import hashlib
import hmac
import json
import math
from decimal import Decimal, localcontext
import random
import unittest
from auth_api import (issue_token, verify_token, authorized, RateLimiter, ProtectedAPI,
                      b64url, b64url_decode, ISSUER, AUDIENCE)

KEY = b"test-only-public-key-with-32-bytes-or-more"


def signed(payload, header=None):
    header = {"alg": "HS256", "typ": "JWT"} if header is None else header
    raw_header = header if isinstance(header, str) else json.dumps(header, separators=(",", ":"))
    raw_payload = payload if isinstance(payload, str) else json.dumps(payload, separators=(",", ":"))
    h, p = b64url(raw_header.encode()), b64url(raw_payload.encode())
    signature = b64url(hmac.new(KEY, f"{h}.{p}".encode(), hashlib.sha256).digest())
    return f"{h}.{p}.{signature}"


def claims():
    return {"sub": "anna", "role": "operator", "iss": ISSUER, "aud": AUDIENCE,
            "iat": 1000, "nbf": 1000, "exp": 1060}


class TokenTests(unittest.TestCase):
    def setUp(self):
        self.token = issue_token("anna", "operator", KEY, ttl=60, now=1000)

    def test_signed_roundtrip_and_original_roles(self):
        payload = verify_token(self.token, KEY, now=1010)
        self.assertEqual(payload, claims())
        self.assertTrue(authorized(payload, "user"))
        self.assertTrue(authorized(payload, "operator"))
        self.assertFalse(authorized(payload, "admin"))

    def test_expiry_exact_boundary_and_fractional_now(self):
        self.assertEqual(verify_token(self.token, KEY, now=1059.999)["sub"], "anna")
        for instant in (1060, 1060.001, 2000):
            with self.subTest(now=instant), self.assertRaises(ValueError):
                verify_token(self.token, KEY, now=instant)

    def test_large_integer_token_times_keep_exact_boundaries(self):
        for start in (2**53 - 1, 2**53, 2**53 + 1, 2**63, 10**100):
            with self.subTest(start=start):
                token = issue_token("anna", "user", KEY, ttl=1, now=start)
                payload = verify_token(token, KEY, now=start)
                self.assertEqual(payload["iat"], start)
                self.assertEqual(payload["exp"], start + 1)
                with self.assertRaisesRegex(ValueError, "non ancora valido"):
                    verify_token(token, KEY, now=start - 1)
                with self.assertRaisesRegex(ValueError, "scaduto"):
                    verify_token(token, KEY, now=start + 1)

    def test_100_seeded_large_integer_token_boundaries(self):
        rng = random.Random(66067)
        for case in range(100):
            with self.subTest(case=case):
                start = 2**rng.randint(53, 160) + rng.randrange(10000)
                ttl = rng.randint(1, 3600)
                token = issue_token("anna", "user", KEY, ttl=ttl, now=start)
                self.assertEqual(verify_token(token, KEY, now=start + ttl - 1)["iat"], start)
                with self.assertRaisesRegex(ValueError, "scaduto"):
                    verify_token(token, KEY, now=start + ttl)

    def test_wrong_key_and_tampered_payload(self):
        with self.assertRaises(ValueError):
            verify_token(self.token, b"x" * 32, now=1001)
        head, payload, signature = self.token.split(".")
        changed = claims()
        changed["role"] = "admin"
        with self.assertRaises(ValueError):
            verify_token(head + "." + b64url(json.dumps(changed).encode()) + "." + signature, KEY, now=1001)

    def test_algorithm_and_header_allowlist(self):
        for header in ({"alg": "none", "typ": "JWT"}, {"alg": "HS512", "typ": "JWT"},
                       {"alg": "HS256", "typ": "other"}, {"alg": "HS256", "typ": "JWT", "kid": "x"},
                       {"alg": "HS256", "typ": "JWT", "crit": ["x"]}, []):
            with self.subTest(header=header), self.assertRaises(ValueError):
                verify_token(signed(claims(), header), KEY, now=1001)

    def test_issuer_and_audience_are_required(self):
        for field in ("iss", "aud"):
            changed = claims()
            changed[field] = "unrelated"
            with self.subTest(field=field), self.assertRaises(ValueError):
                verify_token(signed(changed), KEY, now=1001)
        with self.assertRaises(ValueError):
            verify_token(self.token, KEY, now=1001, audience="another-api")

    def test_missing_unknown_and_mistyped_claims(self):
        cases = []
        for name in claims():
            c = claims()
            del c[name]
            cases.append(c)
        for name, value in (("exp", True), ("exp", "1060"), ("exp", 1060.0), ("role", []),
                            ("role", "root"), ("sub", ""), ("iat", -1), ("nbf", 2000), ("exp", 9999)):
            c = claims()
            c[name] = value
            cases.append(c)
        c = claims()
        c["extra"] = 1
        cases.append(c)
        for index, c in enumerate(cases):
            with self.subTest(case=index), self.assertRaises(ValueError):
                verify_token(signed(c), KEY, now=1001)

    def test_not_before_and_issued_at(self):
        with self.assertRaises(ValueError):
            verify_token(self.token, KEY, now=999.999)
        changed = claims()
        changed["nbf"] = 1010
        with self.assertRaises(ValueError):
            verify_token(signed(changed), KEY, now=1009)
        self.assertEqual(verify_token(signed(changed), KEY, now=1010)["nbf"], 1010)

    def test_json_duplicates_and_nonfinite_values_rejected(self):
        raw = json.dumps(claims())[:-1] + ', "exp": 1090}'
        for token in (signed(raw), signed('{"exp":NaN}'), signed("[]"), signed("not-json"),
                      signed(claims(), '{"alg":"HS256","alg":"HS256","typ":"JWT"}')):
            with self.subTest(token=token[:25]), self.assertRaises(ValueError):
                verify_token(token, KEY, now=1001)

    def test_malformed_tokens_fail_as_value_error(self):
        for token in (None, 123, "", "a", "a.b", "a.b.c.d", "é.b.c", "a.!.$", "a" * 4097):
            with self.subTest(token=str(token)[:20]), self.assertRaises(ValueError):
                verify_token(token, KEY, now=1001)

    def test_base64url_is_strict_and_canonical(self):
        self.assertEqual(b64url_decode(b64url(b"abc\x00")), b"abc\x00")
        for value in ("", "a", "YQ==", "YQ\n", "YR", "é"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                b64url_decode(value)

    def test_configuration_rejected(self):
        for key in ("short", b"", None):
            with self.subTest(key=key), self.assertRaises(ValueError):
                issue_token("anna", "user", key, now=1000)
        for ttl in (0, -1, 3601, True, 1.5):
            with self.subTest(ttl=ttl), self.assertRaises(ValueError):
                issue_token("anna", "user", KEY, ttl=ttl, now=1000)
        for instant in (float("nan"), float("inf"), -1, True):
            with self.subTest(instant=instant), self.assertRaises(ValueError):
                verify_token(self.token, KEY, now=instant)

    def test_unknown_roles_deny_instead_of_escalating(self):
        for payload, required in (({}, "user"), ({"role": "root"}, "user"), ({"role": []}, "user"),
                                  ({"role": "admin"}, "root"), (None, "user"), ({"role": "admin"}, [])):
            with self.subTest(payload=payload, required=required):
                self.assertFalse(authorized(payload, required))

    def test_100_seeded_lifetime_and_tampering_cases(self):
        rng = random.Random(66066)
        for case in range(100):
            with self.subTest(case=case):
                start, ttl = rng.randrange(100000), rng.randint(1, 3600)
                user, role = "utente-" + str(case), rng.choice(("user", "operator", "admin"))
                token = issue_token(user, role, KEY, ttl=ttl, now=start)
                self.assertEqual(verify_token(token, KEY, now=start + ttl / 2)["sub"], user)
                with self.assertRaises(ValueError):
                    verify_token(token, KEY, now=start + ttl)
                parts = token.split(".")
                sig = bytearray(b64url_decode(parts[2]))
                sig[rng.randrange(len(sig))] ^= 1 << rng.randrange(8)
                with self.assertRaises(ValueError):
                    verify_token(parts[0] + "." + parts[1] + "." + b64url(bytes(sig)), KEY, now=start)


class RateLimitTests(unittest.TestCase):
    def test_original_limit_and_boundary(self):
        rate = RateLimiter(2, 10)
        self.assertTrue(rate.allow("anna", 1))
        self.assertTrue(rate.allow("anna", 2))
        self.assertFalse(rate.allow("anna", 3))
        self.assertTrue(rate.allow("anna", 11))
        self.assertEqual(list(rate.events["anna"]), [2, 11])

    def test_keys_are_independent_and_capacity_bounded(self):
        rate = RateLimiter(1, 10, max_keys=2)
        self.assertTrue(rate.allow("a", 0))
        self.assertTrue(rate.allow("b", 0))
        self.assertFalse(rate.allow("c", 0))
        self.assertFalse(rate.allow("a", 1))
        self.assertTrue(rate.allow("c", 10))
        self.assertEqual(set(rate.events), {"c"})

    def test_clock_reversal_rejected_without_append(self):
        rate = RateLimiter(2, 10)
        rate.allow("a", 10)
        with self.assertRaises(ValueError):
            rate.allow("a", 9)
        self.assertEqual(list(rate.events["a"]), [10])

    def test_extreme_windows_keep_same_time_requests(self):
        cases = ((1.0, 1e-20), (1.0, math.ulp(0.0)),
                 (1e308, 10.0), (2**53 + 1, 0.5))
        for instant, window in cases:
            with self.subTest(now=instant, window=window):
                rate = RateLimiter(1, window)
                self.assertEqual([rate.allow("a", instant) for _ in range(3)], [True, False, False])
                self.assertEqual(list(rate.events["a"]), [instant])

    def test_rounded_cutoff_does_not_expire_recent_event(self):
        before = math.nextafter(1.0, 0.0)
        rate = RateLimiter(1, 1.2e-16)
        self.assertTrue(rate.allow("a", before))
        # before è ancora nella finestra; la sottrazione float arrotonderebbe a before.
        self.assertFalse(rate.allow("a", 1.0))
        self.assertTrue(rate.allow("a", math.nextafter(1.0, math.inf)))

    def test_large_integer_limiter_boundary_is_exact(self):
        for start in (2**53, 2**53 + 1, 2**63, 10**100):
            with self.subTest(start=start):
                rate = RateLimiter(1, 1)
                self.assertTrue(rate.allow("a", start))
                self.assertEqual(rate.last_time, start)
                self.assertFalse(rate.allow("a", start))
                self.assertTrue(rate.allow("a", start + 1))
                self.assertEqual(list(rate.events["a"]), [start + 1])

    def test_100_seeded_fractional_sequences_against_decimal_reference(self):
        rng = random.Random(66661)
        for case in range(100):
            with self.subTest(case=case), localcontext() as context:
                # Precisione sufficiente a rappresentare esattamente anche tutti i float subnormali.
                context.prec = 1500
                instant = math.ldexp(rng.uniform(1.0, 1.9), rng.choice((-200, -5, 0, 53, 1020)))
                window = rng.choice((1e-20, math.ulp(0.0), math.ulp(instant), 0.1, 0.125, 10.0))
                limit = rng.randint(1, 4)
                rate, reference = RateLimiter(limit, window), []
                exact_window = Decimal.from_float(window)
                for _ in range(40):
                    if rng.randrange(3):
                        instant = math.nextafter(instant, math.inf)
                    exact_now = Decimal.from_float(instant)
                    reference = [event for event in reference if exact_now - event < exact_window]
                    expected = len(reference) < limit
                    self.assertEqual(rate.allow("a", instant), expected)
                    if expected:
                        reference.append(exact_now)
                    self.assertEqual(len(rate.events.get("a", ())), len(reference))

    def test_invalid_parameters(self):
        for limit, window in ((0, 10), (True, 10), (2, 0), (2, float("nan")), (2, float("inf"))):
            with self.subTest(limit=limit, window=window), self.assertRaises(ValueError):
                RateLimiter(limit, window)
        rate = RateLimiter(2, 10)
        for key in ("", [], "x" * 129):
            with self.subTest(key=key), self.assertRaises(ValueError):
                rate.allow(key, 0)

    def test_100_seeded_sequences_against_reference(self):
        rng = random.Random(66660)
        for case in range(100):
            with self.subTest(case=case):
                limit, window = rng.randint(1, 8), rng.randint(1, 20)
                rate, reference, instant = RateLimiter(limit, window), {}, 0
                for _ in range(60):
                    instant += rng.randint(0, 3)
                    key = rng.choice(("a", "b", "c"))
                    valid = [t for t in reference.get(key, []) if instant - window < t]
                    expected = len(valid) < limit
                    self.assertEqual(rate.allow(key, instant), expected)
                    if expected:
                        valid.append(instant)
                    reference[key] = valid
                    self.assertLessEqual(len(rate.events.get(key, [])), limit)

    def test_local_pipeline_denies_before_resource(self):
        token = issue_token("anna", "operator", KEY, now=1000, ttl=60)
        api = ProtectedAPI(KEY, RateLimiter(3, 10))
        self.assertEqual(api.request("a", token, "user", now=1001, rate_now=1), 200)
        self.assertEqual(api.request("a", token, "admin", now=1001, rate_now=2), 403)
        self.assertEqual(api.request("a", "invalid", "user", now=1001, rate_now=3), 401)
        self.assertEqual(api.request("a", token, "user", now=1001, rate_now=4), 429)
        self.assertEqual(api.request("a", token, "user", now=1060, rate_now=20), 401)
