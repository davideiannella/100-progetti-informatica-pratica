from dataclasses import dataclass

@dataclass
class Node:
    key: object = None
    value: object = None
    prev: 'Node|None' = None
    next: 'Node|None' = None

class LRUCache:

    def __init__(self, capacity: int):
        if type(capacity) is not int or capacity < 0:
            raise ValueError('capacity must be >= 0')
        self.capacity = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, n):
        n.prev.next = n.next
        n.next.prev = n.prev

    def _add_front(self, n):
        n.next = self.head.next
        n.prev = self.head
        self.head.next.prev = n
        self.head.next = n

    def get(self, key, default=None):
        n = self.map.get(key)
        if n is None:
            return default
        self._remove(n)
        self._add_front(n)
        return n.value

    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.map:
            n = self.map[key]
            n.value = value
            self._remove(n)
            self._add_front(n)
            return
        n = Node(key, value)
        self.map[key] = n
        self._add_front(n)
        if len(self.map) > self.capacity:
            victim = self.tail.prev
            self._remove(victim)
            del self.map[victim.key]

    def keys_mru_to_lru(self):
        out = []
        n = self.head.next
        while n is not self.tail:
            out.append(n.key)
            n = n.next
        return out
