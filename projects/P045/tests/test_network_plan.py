import unittest
from ipaddress import IPv4Network
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1]/'src'))
from network_plan import build_plan, validate_plan
class NetworkPlanTest(unittest.TestCase):
    def setUp(self): self.plan=build_plan(); self.base=IPv4Network('10.20.0.0/22')
    def test_all_inside_supernet(self): self.assertTrue(all(s.network.subnet_of(self.base) for s in self.plan))
    def test_no_overlaps(self):
        for i,a in enumerate(self.plan):
            for b in self.plan[i+1:]: self.assertFalse(a.network.overlaps(b.network))
    def test_capacity(self):
        for s in self.plan: self.assertGreaterEqual(s.usable_hosts,s.hosts_required)
    def test_students_is_slash_23(self): self.assertEqual(next(s for s in self.plan if s.name=='Wi-Fi studenti').network.prefixlen,23)
    def test_labs_are_slash_25(self): self.assertEqual([s.network.prefixlen for s in self.plan if 'Laboratorio' in s.name],[25,25])
    def test_management_is_slash_28(self): self.assertEqual(next(s for s in self.plan if s.name=='Management').network.prefixlen,28)
    def test_validate_plan(self): self.assertTrue(validate_plan())
if __name__=='__main__': unittest.main()
