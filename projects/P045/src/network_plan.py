from dataclasses import dataclass
from ipaddress import IPv4Network
from typing import List
@dataclass(frozen=True)
class Segment:
    name: str
    hosts_required: int
    network: IPv4Network
    @property
    def usable_hosts(self): return max(self.network.num_addresses-2,0)
    @property
    def gateway(self): return str(next(self.network.hosts()))
def build_plan() -> List[Segment]:
    return [
        Segment('Wi-Fi studenti',300,IPv4Network('10.20.0.0/23')),
        Segment('Laboratorio 1',120,IPv4Network('10.20.2.0/25')),
        Segment('Laboratorio 2',120,IPv4Network('10.20.2.128/25')),
        Segment('Docenti',60,IPv4Network('10.20.3.0/26')),
        Segment('Segreteria',30,IPv4Network('10.20.3.64/27')),
        Segment('Server',20,IPv4Network('10.20.3.96/27')),
        Segment('Management',10,IPv4Network('10.20.3.128/28')),
    ]
def validate_plan(supernet='10.20.0.0/22'):
    base=IPv4Network(supernet); plan=build_plan()
    for s in plan:
        if not s.network.subnet_of(base): raise ValueError('subnet fuori supernet')
        if s.usable_hosts < s.hosts_required: raise ValueError('host insufficienti')
    for i,a in enumerate(plan):
        for b in plan[i+1:]:
            if a.network.overlaps(b.network): raise ValueError('overlap')
    return True
if __name__=='__main__':
    validate_plan()
    for s in build_plan(): print(s.name, s.network, s.gateway, s.usable_hosts)
