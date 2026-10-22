from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parents[1]/'src'))
from transport_lab import tcp_roundtrip,udp_roundtrip
for data in [b'',bytes(range(256))*1024]: assert tcp_roundtrip(data)==data
for data in [b'',bytes(range(256))*24]: assert udp_roundtrip(data)==data
try: udp_roundtrip(b'x'*65508)
except ValueError: pass
else: raise AssertionError('oversize')
print('P048 socket reali vuoti, binari e oltre 4096 byte PASS')
