import random
import sqlite3
import unittest
from safe_search import make_db, find_user


class ParameterizedQueryTests(unittest.TestCase):
    def setUp(self):
        self.con = make_db()
        self.addCleanup(self.con.close)

    def snapshot(self):
        return self.con.execute("SELECT id,username,role FROM user ORDER BY id").fetchall()

    def test_known_and_unknown_users(self):
        self.assertEqual(find_user(self.con, "anna"), ("anna", "user"))
        self.assertEqual(find_user(self.con, "mario"), ("mario", "admin"))
        self.assertIsNone(find_user(self.con, "missing"))

    def test_seed_transaction_is_committed(self):
        self.assertFalse(self.con.in_transaction)
        self.con.rollback()
        self.assertEqual(len(self.snapshot()), 2)

    def test_sql_syntax_is_only_data(self):
        before = self.snapshot()
        for value in ("' OR 1=1 --", "'; DROP TABLE user; --", '" OR "1"="1', "%", "_", "--", "\x00", "anna'", ""):
            with self.subTest(value=value):
                self.assertIsNone(find_user(self.con, value))
                self.assertEqual(self.snapshot(), before)

    def test_metacharacters_can_be_valid_literal_username(self):
        literal = "d'angelo;--"
        with self.con:
            self.con.execute("INSERT INTO user(username,role) VALUES (?,?)", (literal, "user"))
        self.assertEqual(find_user(self.con, literal), (literal, "user"))
        self.assertIsNone(find_user(self.con, "d'angelo"))

    def test_unicode_and_exact_case(self):
        with self.con:
            self.con.execute("INSERT INTO user(username,role) VALUES (?,?)", ("Zoë 東京", "user"))
        self.assertEqual(find_user(self.con, "Zoë 東京"), ("Zoë 東京", "user"))
        self.assertIsNone(find_user(self.con, "ANNA"))
        self.assertIsNone(find_user(self.con, " anna "))

    def test_input_types_and_length(self):
        for value in (None, 1, b"anna", ["anna"], True):
            with self.subTest(value=value), self.assertRaises(TypeError):
                find_user(self.con, value)
        self.assertIsNone(find_user(self.con, "x" * 128))
        with self.assertRaises(ValueError):
            find_user(self.con, "x" * 129)

    def test_closed_connection_error_is_not_hidden(self):
        self.con.close()
        with self.assertRaises(sqlite3.ProgrammingError):
            find_user(self.con, "anna")

    def test_100_seeded_literal_roundtrips(self):
        rng = random.Random(64064)
        alphabet = "ab'\";-%_()=/\\\x00à東京"
        for case in range(100):
            with self.subTest(case=case):
                value = str(case) + ":" + "".join(rng.choice(alphabet) for _ in range(rng.randrange(1, 50)))
                with self.con:
                    self.con.execute("INSERT INTO user(username,role) VALUES (?,?)", (value, "user"))
                before = self.snapshot()
                self.assertEqual(find_user(self.con, value), (value, "user"))
                self.assertIsNone(find_user(self.con, value + "!"))
                self.assertEqual(self.snapshot(), before)
