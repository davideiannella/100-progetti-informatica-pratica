import sys,pathlib
sys.path.append(str(pathlib.Path(__file__).parents[1]/"src"))
from transport_lab import tcp_roundtrip, udp_roundtrip, simulated_udp_delivery

assert tcp_roundtrip(b"abc") == b"abc"
assert udp_roundtrip(b"xyz") == b"xyz"
assert simulated_udp_delivery([1,2,3,4,5,6],3) == [1,2,4,5]
print("P048: TCP/UDP localhost lab PASS")
