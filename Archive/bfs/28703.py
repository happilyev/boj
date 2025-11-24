import sys
from collections import deque

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

m = max(a)
a.sort()
res = m - a[0]
dq = deque([a[0]])
visited = set()
visited.add(res)

while dq:
    temp = dq.popleft()
    for o in a:
        if o not in visited:
            m = max(m, o*2)
            if m>o*2:
                res = min(res, m-o*2)
            if o*2>m:
                res = min(res, o*2-m)
            visited.add(o)
            dq.append(o)

print(res)
