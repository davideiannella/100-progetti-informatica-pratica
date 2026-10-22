from collections import deque

def checked(refs, frames):
    if type(frames) is not int or frames <= 0:
        raise ValueError("frames intero positivo")
    refs = list(refs)
    if any(type(p) is not int or p < 0 for p in refs):
        raise ValueError("pagine intere non negative")
    return refs

def fifo(refs, frames):
    refs = checked(refs, frames)
    if frames<=0: raise ValueError("frames")
    mem=deque(); present=set(); faults=0
    for p in refs:
        if p not in present:
            faults+=1
            if len(mem)==frames:
                old=mem.popleft(); present.remove(old)
            mem.append(p); present.add(p)
    return faults

def lru(refs, frames):
    refs = checked(refs, frames)
    if frames<=0: raise ValueError("frames")
    mem=[]; faults=0
    for p in refs:
        if p in mem:
            mem.remove(p); mem.append(p)
        else:
            faults+=1
            if len(mem)==frames: mem.pop(0)
            mem.append(p)
    return faults

def clock(refs, frames):
    refs = checked(refs, frames)
    if frames<=0: raise ValueError("frames")
    pages=[None]*frames; use=[0]*frames; hand=0; faults=0
    for p in refs:
        if p in pages:
            use[pages.index(p)]=1
            continue
        faults+=1
        while pages[hand] is not None and use[hand]:
            use[hand]=0; hand=(hand+1)%frames
        pages[hand]=p; use[hand]=1; hand=(hand+1)%frames
    return faults
