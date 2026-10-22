import unittest
from pathlib import Path
import sys
from fastapi import HTTPException
from pydantic import ValidationError

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))
import app as api

class ApiLogicTest(unittest.TestCase):
    def setUp(self): api.items.clear()
    def test_health(self): self.assertEqual(api.health(), {"status":"ok"})
    def test_create_and_get(self):
        v=api.upsert_item(1, api.ItemIn(name="router", quantity=2))
        self.assertEqual(v["name"],"router")
        self.assertEqual(api.get_item(1)["quantity"],2)
    def test_invalid_id(self):
        with self.assertRaises(HTTPException): api.upsert_item(0, api.ItemIn(name="x",quantity=1))
    def test_missing_item(self):
        with self.assertRaises(HTTPException): api.get_item(99)
    def test_negative_quantity_rejected(self):
        with self.assertRaises(ValidationError): api.ItemIn(name="x",quantity=-1)

if __name__=="__main__": unittest.main()
