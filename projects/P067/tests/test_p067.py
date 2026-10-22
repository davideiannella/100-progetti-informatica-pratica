import hashlib
import pathlib
import ssl
import stat
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))
from cert_check import create_lab, fingerprint_sha256, generate_and_verify, tls_exchange
from cryptography import x509
from cryptography.hazmat.primitives import serialization


class TLSLabTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="p067-test-")
        self.addCleanup(self.temp.cleanup)
        self.base = pathlib.Path(self.temp.name)
        self.p = create_lab(self.base / "valid")

    def exchange(self, paths=None, **kwargs):
        p = self.p if paths is None else paths
        return tls_exchange(p["cert"], p["key"], p["ca"], **kwargs)

    def test_real_handshake_and_echo(self):
        data = b"ordine=42\x00\xff"
        result = self.exchange(payload=data)
        self.assertEqual(result["payload"], data)
        self.assertIn(result["tls_version"], {"TLSv1.2", "TLSv1.3"})
        self.assertTrue(result["cipher"])
        self.assertEqual(result["peer_sha256"], fingerprint_sha256(self.p["cert"]))

    def test_hostname_rejected(self):
        with self.assertRaises(ssl.SSLCertVerificationError): self.exchange(hostname="altro.invalid")

    def test_ip_is_not_dns_san(self):
        with self.assertRaises(ssl.SSLCertVerificationError): self.exchange(hostname="127.0.0.1")

    def test_unknown_ca_rejected(self):
        other = create_lab(self.base / "other")
        with self.assertRaises(ssl.SSLCertVerificationError):
            tls_exchange(self.p["cert"], self.p["key"], other["ca"])

    def test_expired_certificate_rejected(self):
        with self.assertRaises(ssl.SSLCertVerificationError):
            self.exchange(create_lab(self.base / "expired", validity="expired"))

    def test_future_certificate_rejected(self):
        with self.assertRaises(ssl.SSLCertVerificationError):
            self.exchange(create_lab(self.base / "future", validity="future"))

    def test_wrong_extended_key_usage_rejected(self):
        with self.assertRaises(ssl.SSLCertVerificationError):
            self.exchange(create_lab(self.base / "client", server_auth=False))

    def test_payload_boundaries(self):
        for data in (b"", bytes(range(256)) * 256):
            with self.subTest(size=len(data)): self.assertEqual(self.exchange(payload=data)["payload"], data)
        for invalid in ("text", bytearray(b"x"), b"x" * 65537):
            with self.subTest(type=type(invalid).__name__):
                with self.assertRaises(ValueError): self.exchange(payload=invalid)

    def test_fingerprint_is_sha256_of_der(self):
        cert = x509.load_pem_x509_certificate(self.p["cert"].read_bytes())
        expected = hashlib.sha256(cert.public_bytes(serialization.Encoding.DER)).hexdigest()
        self.assertEqual(fingerprint_sha256(self.p["cert"]), expected)

    def test_new_files_and_private_key_mode(self):
        self.assertEqual(stat.S_IMODE(self.p["key"].stat().st_mode), 0o600)
        before = self.p["key"].read_bytes()
        with self.assertRaises(FileExistsError): create_lab(self.base / "valid")
        self.assertEqual(self.p["key"].read_bytes(), before)

    def test_wrong_private_key_rejected(self):
        other = create_lab(self.base / "other")
        with self.assertRaises(ssl.SSLError): tls_exchange(self.p["cert"], other["key"], self.p["ca"])

    def test_malformed_certificate_rejected(self):
        path = self.base / "invalid.pem"; path.write_text("not a PEM")
        with self.assertRaises(ValueError): fingerprint_sha256(path)
        with self.assertRaises(ssl.SSLError): tls_exchange(path, self.p["key"], self.p["ca"])

    def test_compatibility_api_normalizes_fingerprint(self):
        verification, fingerprint = generate_and_verify(self.base / "compat")
        self.assertIn(": OK", verification)
        self.assertRegex(fingerprint, r"^SHA256 Fingerprint=(?:[0-9A-F]{2}:){31}[0-9A-F]{2}$")

    def test_invalid_lab_parameters(self):
        for kwargs in ({"validity": "forever"}, {"server_auth": 1}):
            with self.subTest(kwargs=kwargs):
                with self.assertRaises(ValueError): create_lab(self.base / "bad", **kwargs)


if __name__ == "__main__": unittest.main(verbosity=2)
