from dataclasses import dataclass

@dataclass(frozen=True)
class Zone:
    name: str
    devices: int
    target_devices_per_ap: int

    def aps_needed(self):
        if self.devices <= 0 or self.target_devices_per_ap <= 0:
            raise ValueError("valori non validi")
        return (self.devices + self.target_devices_per_ap - 1)//self.target_devices_per_ap

def non_overlapping_24ghz():
    return [1,6,11]

def plan():
    zones=[
        Zone("ricevimento",24,20),
        Zone("corsie A-B",70,25),
        Zone("corsie C-D",65,25),
        Zone("spedizioni",40,20),
    ]
    return {z.name:z.aps_needed() for z in zones}
