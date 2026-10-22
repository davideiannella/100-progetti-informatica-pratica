import html
from html.parser import HTMLParser
import random
import unittest
from web_defense import safe_html, new_csrf_token, verify_csrf, content_security_policy, LocalWebApp


class Tags(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)


class WebDefenseTests(unittest.TestCase):
    def setUp(self):
        self.app = LocalWebApp(session_ttl=60)
        self.session, self.token = self.app.start_session(now=1000)

    def test_html_encoding_quotes_ampersand_and_script(self):
        self.assertEqual(safe_html('<script>alert(1)</script>'), '&lt;script&gt;alert(1)&lt;/script&gt;')
        self.assertEqual(safe_html('"\'&<>'), '&quot;&#x27;&amp;&lt;&gt;')
        with self.assertRaises(TypeError):
            safe_html(None)

    def test_request_modifies_state_and_encodes_output(self):
        result = self.app.update_message(self.session, self.token, '<b>ciao</b>', now=1001)
        self.assertEqual(result.status, 200)
        self.assertEqual(self.app.sessions[self.session]["message"], '<b>ciao</b>')
        parser = Tags()
        parser.feed(result.body)
        self.assertEqual(parser.tags, ["p"])
        self.assertEqual(result.headers["Content-Security-Policy"], content_security_policy())

    def test_missing_wrong_and_malformed_csrf_deny_without_mutation(self):
        for value in (None, "", [], 123, self.token + "x", "é" * 43, b"x" * 43):
            with self.subTest(value=str(value)[:30]):
                self.assertFalse(verify_csrf(self.token, value))
                self.assertEqual(self.app.update_message(self.session, value, "changed", now=1001).status, 403)
                self.assertEqual(self.app.sessions[self.session]["message"], "")

    def test_cross_session_token_is_rejected(self):
        other, other_token = self.app.start_session(now=1000)
        self.assertNotEqual(self.token, other_token)
        self.assertEqual(self.app.update_message(other, self.token, "changed", now=1001).status, 403)
        self.assertEqual(self.app.update_message(self.session, other_token, "changed", now=1001).status, 403)

    def test_get_cannot_modify_state(self):
        self.assertEqual(self.app.update_message(self.session, self.token, "changed", method="GET", now=1001).status, 405)
        self.assertEqual(self.app.sessions[self.session]["message"], "")

    def test_expiration_exact_boundary(self):
        self.assertEqual(self.app.update_message(self.session, self.token, "ok", now=1059).status, 200)
        self.assertEqual(self.app.update_message(self.session, self.token, "no", now=1060).status, 403)
        self.assertNotIn(self.session, self.app.sessions)

    def test_token_reusable_inside_its_session(self):
        for instant in (1001, 1002):
            self.assertEqual(self.app.update_message(self.session, self.token, "ok", now=instant).status, 200)

    def test_logout_invalidates_csrf(self):
        self.app.logout(self.session)
        self.assertEqual(self.app.update_message(self.session, self.token, "changed", now=1001).status, 403)

    def test_input_limits_and_unknown_session(self):
        self.assertEqual(self.app.update_message(self.session, self.token, "x" * 1000, now=1001).status, 200)
        for value in ("x" * 1001, None):
            with self.subTest(length=None if value is None else len(value)):
                self.assertEqual(self.app.update_message(self.session, self.token, value, now=1001).status, 400)
        self.assertEqual(self.app.update_message([], self.token, "x", now=1001).status, 403)
        for value in (0, -1, float("nan"), float("inf"), True):
            with self.subTest(ttl=value), self.assertRaises(ValueError):
                LocalWebApp(session_ttl=value)

    def test_session_expiry_overflow_and_precision_rejected(self):
        for ttl, instant in ((1e308, 1e308), (60, 1e308)):
            with self.subTest(ttl=ttl, now=instant):
                app = LocalWebApp(session_ttl=ttl)
                with self.assertRaises(ValueError):
                    app.start_session(now=instant)
                self.assertEqual(app.sessions, {})

    def test_csp_is_on_failure_responses_too(self):
        response = self.app.update_message(self.session, None, "no", now=1001)
        self.assertIn("script-src 'none'", response.headers["Content-Security-Policy"])
        self.assertIn("frame-ancestors 'none'", response.headers["Content-Security-Policy"])
        self.assertEqual(response.headers["Content-Type"], "text/html; charset=utf-8")

    def test_100_seeded_html_roundtrips(self):
        rng = random.Random(65065)
        alphabet = "<>\"'&;abc àè東京\n/="
        for case in range(100):
            with self.subTest(case=case):
                text = "".join(rng.choice(alphabet) for _ in range(rng.randrange(200)))
                encoded = safe_html(text)
                self.assertNotIn("<", encoded)
                self.assertNotIn(">", encoded)
                self.assertEqual(html.unescape(encoded), text)
                response = self.app.update_message(self.session, self.token, text, now=1001)
                parser = Tags()
                parser.feed(response.body)
                self.assertEqual(parser.tags, ["p"])

    def test_generated_token_properties(self):
        observed = set()
        for case in range(10):
            with self.subTest(case=case):
                first, second = new_csrf_token(), new_csrf_token()
                self.assertTrue(verify_csrf(first, first))
                self.assertFalse(verify_csrf(first, second))
                self.assertNotIn(first, observed)
                observed.add(first)
