from __future__ import annotations
from dataclasses import dataclass
import heapq
import math
from typing import Dict, List, Optional, Tuple
VALID_PRIORITIES = {1, 2, 3}

@dataclass(frozen=True)
class Ticket:
    ticket_id: str
    priority: int
    issued_at: float
    sequence: int

@dataclass(frozen=True)
class ServedTicket:
    ticket: Ticket
    served_at: float
    wait_time: float

class QueueManager:
    """Coda prioritaria con FIFO a parità di priorità.

    Inserimento e chiamata del prossimo ticket usano un heap.
    La cancellazione usa rimozione logica dal dizionario active.
    """

    def __init__(self) -> None:
        self._heap: List[Tuple[int, int, str]] = []
        self._active: Dict[str, Ticket] = {}
        self._served: List[ServedTicket] = []
        self._sequence = 0

    def issue_ticket(self, priority: int, issued_at: float) -> Ticket:
        if type(priority) is not int or priority not in VALID_PRIORITIES:
            raise ValueError('priority must be 1, 2 or 3')
        if isinstance(issued_at, bool) or not isinstance(issued_at, (int, float)) or (not math.isfinite(issued_at)) or (issued_at < 0):
            raise ValueError('issued_at must be non-negative')
        self._sequence += 1
        ticket_id = f'T{self._sequence:04d}'
        ticket = Ticket(ticket_id=ticket_id, priority=priority, issued_at=float(issued_at), sequence=self._sequence)
        self._active[ticket_id] = ticket
        heapq.heappush(self._heap, (priority, ticket.sequence, ticket_id))
        return ticket

    def cancel_ticket(self, ticket_id: str) -> bool:
        """Cancella un ticket ancora in attesa.

        La voce nell'heap viene ignorata alla prossima estrazione.
        """
        return self._active.pop(ticket_id, None) is not None

    def call_next(self, now: float) -> Optional[ServedTicket]:
        if isinstance(now, bool) or not isinstance(now, (int, float)) or (not math.isfinite(now)) or (now < 0):
            raise ValueError('now must be non-negative')
        while self._heap:
            _, _, ticket_id = heapq.heappop(self._heap)
            ticket = self._active.pop(ticket_id, None)
            if ticket is None:
                continue
            if now < ticket.issued_at:
                self._active[ticket_id] = ticket
                heapq.heappush(self._heap, (ticket.priority, ticket.sequence, ticket_id))
                raise ValueError('now cannot be earlier than issued_at')
            served = ServedTicket(ticket=ticket, served_at=float(now), wait_time=float(now) - ticket.issued_at)
            self._served.append(served)
            return served
        return None

    @property
    def waiting_count(self) -> int:
        return len(self._active)

    def statistics(self) -> dict:
        waits = [item.wait_time for item in self._served]
        if not waits:
            return {'served_count': 0, 'average_wait': 0.0, 'max_wait': 0.0}
        return {'served_count': len(waits), 'average_wait': sum(waits) / len(waits), 'max_wait': max(waits)}
