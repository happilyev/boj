import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)
for i in range(1, n+1):
    adj[i].sort()
visited = set()
order = []
stack = [1]
while stack:
    a = stack.pop()
    if a not in visited:
        visited.add(a)
        order.append(a)
        for o in reversed(adj[a]):
            if o not in visited:
                stack.append(o)

print(len(order)-1)

# visited = set()
# dq = deque([v])
# visited.add(v)
# order = []
# while dq:
#     u = dq.popleft()
#     order.append(u)
#     for o in adj[u]:
#         if o not in visited:
#             visited.add(o)
#             dq.append(o)
# print(*order)
