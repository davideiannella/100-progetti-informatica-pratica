import heapq
from dataclasses import dataclass

@dataclass(frozen=True)
class Job:
    id: str
    priority: int
    description: str = ''

class Scheduler:

    def __init__(self):
        self._heap = []
        self._seq = 0

    def add(self, job):
        if type(job.priority) is not int or job.priority < 1:
            raise ValueError('Priorità deve essere >=1')
        heapq.heappush(self._heap, (job.priority, self._seq, job))
        self._seq += 1

    def pop(self):
        if not self._heap:
            return None
        return heapq.heappop(self._heap)[2]

    def __len__(self):
        return len(self._heap)
