import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).parents[1]/"src"))
from segmentation import segment_for_ip, allowed, validate

assert validate()
assert segment_for_ip("10.30.10.50") == "uffici"
assert segment_for_ip("10.30.99.5") == "management"
assert segment_for_ip("192.168.1.1") is None
assert allowed("uffici","server","https")
assert not allowed("guest","server","https")
assert allowed("management","server","ssh")
assert not allowed("produzione","management","ssh")
print("P046: VLAN/subnet/ACL model PASS")
