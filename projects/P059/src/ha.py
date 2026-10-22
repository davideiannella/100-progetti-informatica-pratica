class Backend:
    def __init__(self,name):
        self.name=name; self.healthy=True; self.calls=0
    def handle(self,key):
        if not self.healthy: raise RuntimeError("down")
        self.calls+=1
        return f"{self.name}:{key}"

class LoadBalancer:
    def __init__(self,backends):
        self.backends=backends; self.i=0
    def request(self,key):
        healthy=[b for b in self.backends if b.healthy]
        if not healthy: raise RuntimeError("no healthy backend")
        b=healthy[self.i % len(healthy)]
        self.i+=1
        return b.handle(key)

class Cache:
    def __init__(self): self.data={}
    def get_or_set(self,key,loader):
        if key not in self.data: self.data[key]=loader()
        return self.data[key]
