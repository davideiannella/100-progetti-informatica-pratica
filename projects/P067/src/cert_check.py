"""PKI didattica e handshake TLS reale, esclusivamente su IPv4 loopback."""
from __future__ import annotations

import hashlib
import os
import socket
import ssl
import struct
import tempfile
import threading
from datetime import datetime, timedelta, timezone
from pathlib import Path

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.x509.oid import ExtendedKeyUsageOID, NameOID


def _save_new(path: Path, data: bytes, private: bool = False) -> None:
    """Non sovrascrive file esistenti; la chiave nasce con modo 0600."""
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600 if private else 0o644)
    with os.fdopen(fd, "wb") as stream:
        stream.write(data)


def create_lab(directory, *, validity="valid", server_auth=True):
    """Crea una CA locale e un certificato server SAN localhost, per test."""
    if validity not in {"valid", "expired", "future"}:
        raise ValueError("validity: valid, expired oppure future")
    if type(server_auth) is not bool:
        raise ValueError("server_auth deve essere bool")
    d = Path(directory)
    d.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    ca_key = ec.generate_private_key(ec.SECP256R1())
    server_key = ec.generate_private_key(ec.SECP256R1())
    ca_name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "P067 Laboratory CA")])
    ca = (x509.CertificateBuilder().subject_name(ca_name).issuer_name(ca_name)
          .public_key(ca_key.public_key()).serial_number(x509.random_serial_number())
          .not_valid_before(now - timedelta(days=10)).not_valid_after(now + timedelta(days=10))
          .add_extension(x509.BasicConstraints(ca=True, path_length=0), critical=True)
          .add_extension(x509.KeyUsage(False, False, False, False, False, True, True, False, False), critical=True)
          .add_extension(x509.SubjectKeyIdentifier.from_public_key(ca_key.public_key()), critical=False)
          .sign(ca_key, hashes.SHA256()))
    dates = {"valid": (-1, 1), "expired": (-3, -2), "future": (2, 3)}[validity]
    eku = ExtendedKeyUsageOID.SERVER_AUTH if server_auth else ExtendedKeyUsageOID.CLIENT_AUTH
    cert = (x509.CertificateBuilder()
            .subject_name(x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "localhost")]))
            .issuer_name(ca_name).public_key(server_key.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(now + timedelta(days=dates[0]))
            .not_valid_after(now + timedelta(days=dates[1]))
            .add_extension(x509.BasicConstraints(ca=False, path_length=None), critical=True)
            .add_extension(x509.KeyUsage(True, False, False, False, False, False, False, False, False), critical=True)
            .add_extension(x509.SubjectAlternativeName([x509.DNSName("localhost")]), critical=False)
            .add_extension(x509.ExtendedKeyUsage([eku]), critical=False)
            .add_extension(x509.AuthorityKeyIdentifier.from_issuer_public_key(ca_key.public_key()), critical=False)
            .add_extension(x509.SubjectKeyIdentifier.from_public_key(server_key.public_key()), critical=False)
            .sign(ca_key, hashes.SHA256()))
    paths = {"ca": d / "ca.pem", "cert": d / "cert.pem", "key": d / "key.pem"}
    # La chiave CA non viene salvata: il laboratorio non è un servizio di emissione.
    _save_new(paths["key"], server_key.private_bytes(serialization.Encoding.PEM,
              serialization.PrivateFormat.PKCS8, serialization.NoEncryption()), private=True)
    _save_new(paths["cert"], cert.public_bytes(serialization.Encoding.PEM))
    _save_new(paths["ca"], ca.public_bytes(serialization.Encoding.PEM))
    return paths


def fingerprint_sha256(certfile):
    cert = x509.load_pem_x509_certificate(Path(certfile).read_bytes())
    return cert.fingerprint(hashes.SHA256()).hex()


def _receive_exact(conn, size):
    parts = bytearray()
    while len(parts) < size:
        chunk = conn.recv(size - len(parts))
        if not chunk:
            raise EOFError("frame TLS incompleto")
        parts.extend(chunk)
    return bytes(parts)


def tls_exchange(certfile, keyfile, cafile, *, hostname="localhost", payload=b"ciao TLS"):
    """Autentica il server e restituisce un echo TLS; nessun contatto esterno."""
    if type(payload) is not bytes or len(payload) > 65536:
        raise ValueError("payload: bytes, massimo 65536 byte")
    if not isinstance(hostname, str) or not hostname or "\x00" in hostname:
        raise ValueError("hostname non valido")
    server_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    server_context.minimum_version = ssl.TLSVersion.TLSv1_2
    server_context.load_cert_chain(certfile, keyfile)
    client_context = ssl.create_default_context(cafile=str(cafile))
    client_context.minimum_version = ssl.TLSVersion.TLSv1_2
    server_errors = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
        listener.bind(("127.0.0.1", 0))
        listener.listen(1)
        listener.settimeout(5)
        address = listener.getsockname()

        def serve():
            try:
                raw, _ = listener.accept()
                with raw:
                    raw.settimeout(5)
                    with server_context.wrap_socket(raw, server_side=True) as conn:
                        size = struct.unpack("!I", _receive_exact(conn, 4))[0]
                        if size > 65536:
                            raise ValueError("frame troppo grande")
                        data = _receive_exact(conn, size)
                        conn.sendall(struct.pack("!I", len(data)) + data)
            except (OSError, ValueError, EOFError) as exc:
                server_errors.append(exc)

        worker = threading.Thread(target=serve, name="P067-loopback", daemon=True)
        worker.start()
        try:
            with socket.create_connection(address, timeout=5) as raw:
                with client_context.wrap_socket(raw, server_hostname=hostname) as conn:
                    conn.sendall(struct.pack("!I", len(payload)) + payload)
                    size = struct.unpack("!I", _receive_exact(conn, 4))[0]
                    if size > 65536:
                        raise ValueError("risposta troppo grande")
                    result = {"payload": _receive_exact(conn, size), "tls_version": conn.version(),
                              "cipher": conn.cipher()[0],
                              "peer_sha256": hashlib.sha256(conn.getpeercert(binary_form=True)).hexdigest()}
        finally:
            worker.join(timeout=6)
        if worker.is_alive():
            raise RuntimeError("server locale non terminato")
        if server_errors:
            raise RuntimeError("errore server locale") from server_errors[0]
    return result


def generate_and_verify(tempdir):
    """API storica: ora esegue anche un vero handshake con verifica server."""
    p = create_lab(tempdir)
    result = tls_exchange(p["cert"], p["key"], p["ca"])
    fp = ":".join(result["peer_sha256"][i:i+2].upper() for i in range(0, 64, 2))
    return f"{p['cert']}: OK (TLS loopback)", f"SHA256 Fingerprint={fp}"


def main():
    with tempfile.TemporaryDirectory(prefix="p067-") as d:
        p = create_lab(d)
        r = tls_exchange(p["cert"], p["key"], p["ca"])
        print("TLS verificato:", r["payload"].decode())
        print("Impronta corrispondente:", r["peer_sha256"] == fingerprint_sha256(p["cert"]))
        try:
            tls_exchange(p["cert"], p["key"], p["ca"], hostname="altro.invalid")
        except ssl.SSLCertVerificationError:
            print("Hostname errato: RIFIUTATO")


if __name__ == "__main__":
    main()
