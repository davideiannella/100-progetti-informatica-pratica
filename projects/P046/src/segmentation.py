from dataclasses import dataclass
from ipaddress import IPv4Network, IPv4Address

@dataclass(frozen=True)
class Segment:
    name: str
    vlan: int
    network: IPv4Network

SEGMENTS = {
    "uffici": Segment("uffici", 10, IPv4Network("10.30.10.0/24")),
    "produzione": Segment("produzione", 20, IPv4Network("10.30.20.0/24")),
    "guest": Segment("guest", 30, IPv4Network("10.30.30.0/24")),
    "server": Segment("server", 40, IPv4Network("10.30.40.0/25")),
    "management": Segment("management", 99, IPv4Network("10.30.99.0/28")),
}

ACL = {
    ("uffici", "server"): {"https", "dns"},
    ("produzione", "server"): {"https", "dns"},
    ("guest", "server"): set(),
    ("guest", "uffici"): set(),
    ("management", "server"): {"ssh", "https"},
    ("management", "uffici"): {"ssh"},
}

def segment_for_ip(ip: str):
    addr = IPv4Address(ip)
    for seg in SEGMENTS.values():
        if addr in seg.network:
            return seg.name
    return None

def allowed(src_segment: str, dst_segment: str, service: str) -> bool:
    if src_segment not in SEGMENTS or dst_segment not in SEGMENTS:
        return False
    if not isinstance(service, str) or not service:
        return False
    if src_segment == dst_segment:
        return True
    return service.lower() in ACL.get((src_segment, dst_segment), set())

def validate():
    segs = list(SEGMENTS.values())
    if len({s.vlan for s in segs}) != len(segs):
        raise ValueError("VLAN duplicate")
    for i, a in enumerate(segs):
        for b in segs[i+1:]:
            if a.network.overlaps(b.network):
                raise ValueError("subnet sovrapposte")
    return True
