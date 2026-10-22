class Node:

    def __init__(self):
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        w = word.strip().casefold()
        if not w:
            raise ValueError('Parola vuota')
        n = self.root
        for ch in w:
            n = n.children.setdefault(ch, Node())
        n.end = True

    def autocomplete(self, prefix, limit=10):
        if type(limit) is not int or limit < 0:
            raise ValueError('Limite non valido')
        p = prefix.strip().casefold()
        n = self.root
        for ch in p:
            if ch not in n.children:
                return []
            n = n.children[ch]
        out = []

        def walk(node, s):
            if len(out) >= limit:
                return
            if node.end:
                out.append(s)
            for ch in sorted(node.children):
                walk(node.children[ch], s + ch)
        walk(n, p)
        return out
