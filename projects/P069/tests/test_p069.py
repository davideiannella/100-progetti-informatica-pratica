import itertools
import os
import pathlib
import random
import stat
import sys
import tempfile
import unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))
from hardening_audit import CONFIG_KEYS, audit_config, audit_file, audit_mode


class HardeningTests(unittest.TestCase):
    def test_real_sandbox_files_read_only_audit(self):
        with tempfile.TemporaryDirectory(prefix="p069-test-") as d:
            p = pathlib.Path(d) / "secret.conf"; p.write_text("synthetic")
            for mode in (0o600, 0o400, 0o644, 0o606, 0o777):
                os.chmod(p, mode)
                before = p.stat()
                self.assertEqual(audit_file(p), audit_mode(mode))
                self.assertEqual(p.stat().st_mode, before.st_mode)
                self.assertEqual(p.read_text(), "synthetic")

    def test_symlink_not_followed(self):
        with tempfile.TemporaryDirectory(prefix="p069-test-") as d:
            p = pathlib.Path(d); target = p / "target"; target.write_text("x")
            link = p / "link"; link.symlink_to(target)
            self.assertEqual(audit_file(link), ["symbolic-link"])
            target.unlink()
            self.assertEqual(audit_file(link), ["symbolic-link"])

    def test_non_regular_and_missing(self):
        with tempfile.TemporaryDirectory(prefix="p069-test-") as d:
            self.assertEqual(audit_file(d), ["not-regular-file"])
            with self.assertRaises(FileNotFoundError): audit_file(pathlib.Path(d) / "absent")

    def test_exhaustive_boolean_configurations(self):
        for password, root, updates in itertools.product((False, True), repeat=3):
            config = dict(zip(CONFIG_KEYS, (password, root, updates)))
            result = audit_config(config)
            self.assertEqual("ssh-password-auth-enabled" in result, password)
            self.assertEqual("ssh-root-login-enabled" in result, root)
            self.assertEqual("security-updates-disabled" in result, not updates)
            self.assertEqual(len(result), password + root + (not updates))

    def test_missing_is_explicit_not_pass(self):
        self.assertEqual(audit_config({}), [f"missing:{key}" for key in CONFIG_KEYS])

    def test_strings_bool_and_unknown_config(self):
        for value in ("yes", "no", 0, 1, None, [], {}):
            with self.subTest(value=value):
                with self.assertRaises(ValueError): audit_config({"automatic_security_updates": value})
        with self.assertRaises(ValueError): audit_config({"automatic_security_update": True})
        with self.assertRaises(ValueError): audit_config([])

    def test_mode_contract(self):
        self.assertEqual(audit_mode(0o600), [])
        self.assertEqual(audit_mode(0o644), ["group-readable", "world-readable"])
        for value in (True, -1, 0o10000, 600.0, "0600", None):
            with self.subTest(value=value):
                with self.assertRaises(ValueError): audit_mode(value)


    def test_exhaustive_4096_permission_modes(self):
        expected = {"group-readable": 0o040, "group-writable": 0o020, "group-executable": 0o010,
                    "world-readable": 0o004, "world-writable": 0o002, "world-executable": 0o001,
                    "owner-executable": 0o100, "setuid": 0o4000, "setgid": 0o2000, "sticky-bit": 0o1000}
        for mode in range(0o10000):
            result = audit_mode(mode)
            self.assertEqual(set(result), {name for name, mask in expected.items() if mode & mask})
            self.assertEqual(len(result), len(set(result)))
            self.assertEqual(audit_mode(mode ^ 0o600), result)

if __name__ == "__main__": unittest.main(verbosity=2)
