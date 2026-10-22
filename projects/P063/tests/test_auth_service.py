import base64
from datetime import datetime, timedelta, timezone
import random
import tempfile
import unittest
from pathlib import Path
from auth_service import AuthService, ScryptHasher

SECRET = base64.b32encode(b"12345678901234567890").decode()
PASSWORD = "Password-Molto-Lunga-2026"
NOW = datetime(2026, 10, 10, 12, 0, tzinfo=timezone.utc)


class AuthenticationTests(unittest.TestCase):
    def setUp(self):
        self.auth = AuthService()
        self.addCleanup(self.auth.close)
        self.auth.register("davide", PASSWORD, totp_secret=SECRET)

    def code(self, when=NOW):
        return self.auth.totp_code(SECRET, when)

    def login(self, when=NOW):
        return self.auth.login("davide", PASSWORD, self.code(when), now=when)

    def test_password_is_scrypt_not_cleartext(self):
        stored = self.auth.password_hash_for("davide")
        self.assertNotIn(PASSWORD, stored)
        self.assertTrue(stored.startswith("scrypt$32768$8$3$"))
        self.assertTrue(self.auth.ph.verify(stored, PASSWORD))
        self.assertFalse(self.auth.ph.verify(stored, PASSWORD + "x"))

    def test_unique_salts_for_same_password(self):
        one = self.auth.password_hash_for("davide")
        self.auth.register("anna", PASSWORD, totp_secret=SECRET)
        two = self.auth.password_hash_for("anna")
        self.assertNotEqual(one.split("$")[4], two.split("$")[4])
        self.assertNotEqual(one, two)

    def test_valid_login_and_session(self):
        result = self.login()
        self.assertTrue(result.ok)
        self.assertRegex(result.session_token, r"^[A-Za-z0-9_-]{43}$")
        self.assertTrue(self.auth.validate_session(result.session_token, now=NOW))

    def test_bad_credentials_have_generic_message(self):
        results = [self.auth.login("missing", PASSWORD, self.code(), now=NOW),
                   self.auth.login("davide", "sbagliata", self.code(), now=NOW),
                   self.auth.login("davide", PASSWORD, "invalid", now=NOW)]
        self.assertTrue(all(not result.ok for result in results))
        self.assertEqual(len({result.message for result in results}), 1)

    def test_malformed_totp_is_rejected(self):
        for code in (None, 123456, "12345", "1234567", "１２３４５６", "é12345", b"123456", " 123456"):
            with self.subTest(code=code):
                self.assertFalse(self.auth.verify_totp(SECRET, code, NOW))

    def test_lockout_exact_boundary(self):
        for _ in range(3):
            self.assertFalse(self.auth.login("davide", "wrong", self.code(), now=NOW).ok)
        self.assertFalse(self.login(NOW + timedelta(seconds=299)).ok)
        self.assertTrue(self.login(NOW + timedelta(seconds=300)).ok)

    def test_success_resets_failure_counter(self):
        self.auth.login("davide", "wrong", self.code(), now=NOW)
        self.assertTrue(self.login().ok)
        self.assertEqual(self.auth._row("davide")["failed_attempts"], 0)

    def test_totp_replay_is_rejected(self):
        self.assertTrue(self.login().ok)
        self.assertFalse(self.login().ok)
        self.assertTrue(self.login(NOW + timedelta(seconds=30)).ok)

    def test_replay_state_survives_database_reopen(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = str(Path(tmp) / "auth.sqlite")
            first = AuthService(path)
            first.register("a", PASSWORD, totp_secret=SECRET)
            self.assertTrue(first.login("a", PASSWORD, self.code(), now=NOW).ok)
            first.close()
            second = AuthService(path)
            try:
                self.assertFalse(second.login("a", PASSWORD, self.code(), now=NOW).ok)
            finally:
                second.close()

    def test_session_expires_at_exact_deadline_and_is_removed(self):
        token = self.login().session_token
        self.assertTrue(self.auth.validate_session(token, now=NOW + timedelta(seconds=1799)))
        self.assertFalse(self.auth.validate_session(token, now=NOW + timedelta(seconds=1800)))
        self.assertNotIn(token, self.auth.sessions)

    def test_logout_and_unknown_token(self):
        token = self.login().session_token
        self.auth.logout(token)
        self.auth.logout(token)
        self.assertFalse(self.auth.validate_session(token, now=NOW))
        for value in (None, [], "é", "x" * 43):
            with self.subTest(value=value):
                self.assertFalse(self.auth.validate_session(value, now=NOW))

    def test_registration_constraints_and_duplicate(self):
        for username, password in (("", PASSWORD), ("x" * 129, PASSWORD), ("x", "short"), ("x", "é" * 600)):
            with self.subTest(username=username[:20]), self.assertRaises(ValueError):
                self.auth.register(username, password)
        with self.assertRaises(ValueError):
            self.auth.register("davide", PASSWORD)
        self.assertEqual(self.auth.conn.execute("SELECT count(*) FROM users").fetchone()[0], 1)

    def test_username_normalization_and_password_spaces_preserved(self):
        self.auth.register(" anna ", "  password lunga  ", totp_secret=SECRET)
        self.assertTrue(self.auth.login(" anna ", "  password lunga  ", self.code(), now=NOW).ok)
        self.assertFalse(self.auth.ph.verify(self.auth.password_hash_for("anna"), "password lunga"))

    def test_secret_and_configuration_validation(self):
        for secret in ("JBSWY3DPEHPK3PXP", "invalid!", "", None):
            with self.subTest(secret=secret), self.assertRaises(ValueError):
                self.auth.totp_code(secret, NOW)
        for kwargs in ({"max_failures": 0}, {"lock_minutes": -1}, {"session_minutes": True}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                AuthService(**kwargs)
        with self.assertRaises(ValueError):
            self.auth.totp_code(SECRET, NOW, step=0)
        with self.assertRaises(ValueError):
            self.auth.verify_totp(SECRET, self.code(), NOW, window=3)

    def test_timezone_and_epoch_boundaries(self):
        with self.assertRaises(ValueError):
            self.login(datetime(2026, 1, 1))
        with self.assertRaises(ValueError):
            self.auth.totp_code(SECRET, datetime(1969, 1, 1, tzinfo=timezone.utc))
        epoch = datetime.fromtimestamp(0, timezone.utc)
        self.assertTrue(self.auth.verify_totp(SECRET, self.code(epoch), epoch))

    def test_corrupted_hash_fails_closed(self):
        for record in ("garbage", "scrypt$99999999999$8$3$00$00", "$argon2id$unsupported", None):
            with self.subTest(record=record):
                self.assertFalse(self.auth.ph.verify(record, PASSWORD))
        self.assertFalse(self.auth.ph.verify(self.auth.password_hash_for("davide"), "x" * 2000))

    def test_audit_has_no_secrets(self):
        result = self.login()
        text = str(list(self.auth.audit))
        for secret in (PASSWORD, SECRET, result.session_token, "davide"):
            self.assertNotIn(secret, text)
        self.assertEqual(set(self.auth.audit[0]), {"event", "ok", "time"})


class TOTPReferenceTests(unittest.TestCase):
    def test_rfc6238_sha1_vectors(self):
        vectors = ((59, "94287082"), (1111111109, "07081804"), (1111111111, "14050471"),
                   (1234567890, "89005924"), (2000000000, "69279037"), (20000000000, "65353130"))
        for timestamp, expected in vectors:
            with self.subTest(timestamp=timestamp):
                self.assertEqual(AuthService.totp_code(SECRET, datetime.fromtimestamp(timestamp, timezone.utc), digits=8), expected)

    def test_100_seeded_time_window_properties(self):
        rng = random.Random(63063)
        for case in range(100):
            with self.subTest(case=case):
                base = 30 * rng.randint(1000000, 9000000)
                start = datetime.fromtimestamp(base, timezone.utc)
                later = start + timedelta(seconds=rng.randrange(30))
                code = AuthService.totp_code(SECRET, start)
                self.assertEqual(code, AuthService.totp_code(SECRET, later))
                self.assertTrue(AuthService.verify_totp(SECRET, code, start, window=0))
                self.assertTrue(AuthService.verify_totp(SECRET, code, start + timedelta(seconds=30)))
                self.assertFalse(AuthService.verify_totp(SECRET, code, start + timedelta(seconds=120)))
