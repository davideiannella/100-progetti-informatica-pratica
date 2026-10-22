"""Audit didattico in sola lettura di file riservati e configurazioni sintetiche."""
from collections.abc import Mapping
from pathlib import Path
import stat

CONFIG_KEYS = ("password_authentication", "permit_root_login", "automatic_security_updates")


def audit_mode(mode):
    """Policy per FILE RISERVATI: niente accesso gruppo/altri né esecuzione."""
    if type(mode) is not int or not 0 <= mode <= 0o7777:
        raise ValueError("mode: intero POSIX fra 0 e 0o7777")
    checks = (
        (stat.S_IRGRP, "group-readable"), (stat.S_IWGRP, "group-writable"),
        (stat.S_IXGRP, "group-executable"), (stat.S_IROTH, "world-readable"),
        (stat.S_IWOTH, "world-writable"), (stat.S_IXOTH, "world-executable"),
        (stat.S_IXUSR, "owner-executable"), (stat.S_ISUID, "setuid"),
        (stat.S_ISGID, "setgid"), (stat.S_ISVTX, "sticky-bit"),
    )
    return [label for bit, label in checks if mode & bit]


def audit_file(path):
    """Osserva lstat del nome finale; non segue il symlink finale né legge dati."""
    metadata = Path(path).lstat()
    if stat.S_ISLNK(metadata.st_mode):
        return ["symbolic-link"]
    if not stat.S_ISREG(metadata.st_mode):
        return ["not-regular-file"]
    return audit_mode(stat.S_IMODE(metadata.st_mode))


def audit_config(config):
    """Schema booleano del laboratorio, NON parser di sshd_config."""
    if not isinstance(config, Mapping):
        raise ValueError("config: mapping richiesto")
    if set(config) - set(CONFIG_KEYS):
        raise ValueError("chiave di configurazione sconosciuta")
    if any(type(value) is not bool for value in config.values()):
        raise ValueError("i valori devono essere bool, non stringhe o interi")
    findings = [f"missing:{key}" for key in CONFIG_KEYS if key not in config]
    if config.get("password_authentication") is True:
        findings.append("ssh-password-auth-enabled")
    if config.get("permit_root_login") is True:
        findings.append("ssh-root-login-enabled")
    if config.get("automatic_security_updates") is False:
        findings.append("security-updates-disabled")
    return findings


def main():
    secure = {"password_authentication": False, "permit_root_login": False,
              "automatic_security_updates": True}
    print("Permessi 0600:", audit_mode(0o600))
    print("Permessi 0644:", audit_mode(0o644))
    print("Configurazione completa:", audit_config(secure))
    print("Configurazione incompleta:", audit_config({"password_authentication": False}))


if __name__ == "__main__":
    main()
