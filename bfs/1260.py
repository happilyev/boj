import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)
for i in range(1, n+1):
    adj[i].sort()
visited = set()
order = []
stack = [v]
while stack:
    a = stack.pop()
    if a not in visited:
        visited.add(a)
        order.append(a)
        for o in reversed(adj[a]):
            if o not in visited:
                stack.append(o)

print(*order)

visited = set()
dq = deque([v])
visited.add(v)
order = []
while dq:
    u = dq.popleft()
    order.append(u)
    for o in adj[u]:
        if o not in visited:
            visited.add(o)
            dq.append(o)
print(*order)


