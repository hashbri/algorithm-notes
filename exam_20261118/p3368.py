import math
T=int(input())
a=[]
for i in range(T):
    n=int(input())
    best=float('inf')
    limit=math.isqrt(n+1)
    if limit<2:
        limit=2
    for p in range(2,limit+1):
        q=(n+p-1)//p
        if q<2:
            q=2
        s=p*q
        if s<best:
            best=s
    a.append(best)
for x in range(len(a)):
    print(a[x])

