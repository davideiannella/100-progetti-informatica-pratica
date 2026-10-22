from dataclasses import dataclass
from datetime import datetime
import math

@dataclass(frozen=True)
class Telemetry:
    device_id: str
    ts: datetime
    temperature: float
    humidity: float

    def to_document(self):
        if not isinstance(self.device_id, str) or not self.device_id.strip() or not isinstance(self.ts, datetime):
            raise ValueError('device or timestamp')
        if any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) for v in (self.temperature, self.humidity)):
            raise ValueError('metrics must be finite numbers')
        if not -50 <= self.temperature <= 100:
            raise ValueError('temperature')
        if not 0 <= self.humidity <= 100:
            raise ValueError('humidity')
        return {'deviceId': self.device_id, 'ts': self.ts.isoformat(), 'metrics': {'temperature': self.temperature, 'humidity': self.humidity}}
