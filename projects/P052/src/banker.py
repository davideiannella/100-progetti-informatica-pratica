def safe_sequence(available, allocation, maximum):
    available = list(available)
    allocation = [list(row) for row in allocation]
    maximum = [list(row) for row in maximum]
    if any(type(x) is not int or x < 0 for row in [available] + allocation + maximum for x in row):
        raise ValueError("risorse intere non negative")
    n=len(allocation); m=len(available)
    if len(maximum)!=n or any(len(r)!=m for r in allocation+maximum):
        raise ValueError("dimensioni")
    need=[[maximum[i][j]-allocation[i][j] for j in range(m)] for i in range(n)]
    if any(x<0 for row in need for x in row):
        raise ValueError("maximum < allocation")
    work=list(available); done=[False]*n; seq=[]
    changed=True
    while changed:
        changed=False
        for i in range(n):
            if not done[i] and all(need[i][j] <= work[j] for j in range(m)):
                for j in range(m): work[j]+=allocation[i][j]
                done[i]=True; seq.append(i); changed=True
    return seq if all(done) else None
