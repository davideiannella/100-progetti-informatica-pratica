import hashlib
import pathlib
import random
import sys
import unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))
from incident_response import Incident, RestoreEvidence, STATES, recovery_priority, restore_verified


class IncidentTests(unittest.TestCase):
    def test_complete_workflow_and_audit(self):
        data = b"ordine=42\n"; restored, evidence = restore_verified(data, hashlib.sha256(data).hexdigest())
        self.assertEqual(restored, data)
        incident = Incident()
        for expected in STATES[1:]:
            kwargs = {"recovery_evidence": evidence} if expected == "RECOVERED" else {}
            self.assertEqual(incident.advance(f"azione {expected}", **kwargs), expected)
        self.assertEqual(len(incident.actions), 4)
        self.assertEqual([(a[0], a[1]) for a in incident.actions], list(zip(STATES, STATES[1:])))
        self.assertIsInstance(incident.actions, tuple)

    def test_recover_requires_evidence_and_rejections_do_not_change_state(self):
        incident = Incident(); incident.advance("isolare"); incident.advance("rimuovere")
        for evidence in (None, True, "backup verificato", {}):
            with self.subTest(evidence=evidence):
                with self.assertRaises(ValueError): incident.advance("recuperare", recovery_evidence=evidence)
        self.assertEqual(incident.state, "ERADICATED")
        self.assertEqual(len(incident.actions), 2)

    def test_terminal_state_rejected(self):
        _, evidence = restore_verified(b"", hashlib.sha256(b"").hexdigest())
        incident = Incident()
        incident.advance("isolare"); incident.advance("rimuovere")
        incident.advance("recuperare", recovery_evidence=evidence); incident.advance("migliorare")
        with self.assertRaises(ValueError): incident.advance("extra")
        self.assertEqual(len(incident.actions), 4)

    def test_empty_actions_and_early_evidence_rejected(self):
        incident = Incident()
        for value in ("", " \t", None, True, 42):
            with self.subTest(value=value):
                with self.assertRaises(ValueError): incident.advance(value)
        _, evidence = restore_verified(b"x", hashlib.sha256(b"x").hexdigest())
        with self.assertRaises(ValueError): incident.advance("isolare", recovery_evidence=evidence)
        self.assertEqual(incident.state, "DETECTED")
        self.assertEqual(incident.actions, ())

    def test_malformed_evidence_rejected(self):
        for digest, size in ((None, 1), (5, 1), ("x" * 64, 1), ("a" * 64, -1), ("a" * 64, True)):
            with self.subTest(digest=digest, size=size):
                with self.assertRaises(ValueError): RestoreEvidence(digest, size)

    def test_backup_digest_contract(self):
        for digest in ("", "a" * 63, "z" * 64, None, 0):
            with self.subTest(digest=digest):
                with self.assertRaises(ValueError): restore_verified(b"x", digest)
        for data in ("x", bytearray(b"x"), None):
            with self.subTest(data=data):
                with self.assertRaises(ValueError): restore_verified(data, "0" * 64)
        data = b"x"; digest = hashlib.sha256(data).hexdigest()
        self.assertEqual(restore_verified(data, digest.upper())[0], data)
        with self.assertRaises(ValueError): restore_verified(b"y", digest)

    def test_priority_order_ties_and_copies(self):
        records = [{"name": "a", "criticality": 2, "max_downtime_min": 1},
                   {"name": "b", "criticality": 1, "max_downtime_min": 30},
                   {"name": "c", "criticality": 1, "max_downtime_min": 30},
                   {"name": "d", "criticality": 1, "max_downtime_min": 0}]
        before = [dict(a) for a in records]
        result = recovery_priority(records)
        self.assertEqual([a["name"] for a in result], ["d", "b", "c", "a"])
        self.assertEqual(records, before)
        result[0]["name"] = "modified"
        self.assertEqual(records, before)
        self.assertEqual(recovery_priority([]), [])

    def test_bad_assets_rejected(self):
        good = {"name": "erp", "criticality": 1, "max_downtime_min": 30}
        for field, values in (("name", ("", None)), ("criticality", (True, 0, 6, 1.0, "1")),
                              ("max_downtime_min", (True, -1, 1.5, "30", None))):
            for value in values:
                with self.subTest(field=field, value=value):
                    with self.assertRaises(ValueError): recovery_priority([{**good, field: value}])
        with self.assertRaises(ValueError): recovery_priority([good, good])
        with self.assertRaises(ValueError): recovery_priority([{}])
        with self.assertRaises(ValueError): recovery_priority([None])


def make_seeded_case(seed):
    def test(self):
        rng = random.Random(7000 + seed)
        data = rng.randbytes(rng.randint(1, 4096)); digest = hashlib.sha256(data).hexdigest()
        restored, evidence = restore_verified(data, digest)
        self.assertEqual(restored, data); self.assertEqual(evidence.size, len(data))
        corrupted = bytearray(data); index = rng.randrange(len(data)); corrupted[index] ^= 1 << rng.randrange(8)
        with self.assertRaises(ValueError): restore_verified(bytes(corrupted), digest)
        assets = [{"name": f"asset-{i}", "criticality": rng.randint(1, 5), "max_downtime_min": rng.randint(0, 500)}
                  for i in range(rng.randint(5, 80))]
        ordered = recovery_priority(assets)
        self.assertCountEqual([a["name"] for a in ordered], [a["name"] for a in assets])
        self.assertTrue(all((a["criticality"], a["max_downtime_min"]) <= (b["criticality"], b["max_downtime_min"])
                            for a, b in zip(ordered, ordered[1:])))
        incident = Incident(); incident.advance("contain"); incident.advance("eradicate")
        self.assertEqual(incident.advance("recover", recovery_evidence=evidence), "RECOVERED")
    return test
for seed in range(100): setattr(IncidentTests, f"test_seeded_integrity_and_priority_{seed:03}", make_seeded_case(seed))

if __name__ == "__main__": unittest.main(verbosity=2)
