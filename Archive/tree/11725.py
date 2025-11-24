import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().strip().split())
    tree[a].append(b)
    tree[b].append(a)


dq = deque([1])
order = []
parent = [0]*(n+1)
while dq:
    u = dq.popleft()
    for o in tree[u]:
        if parent[o] == 0:
            parent[o] = u
            dq.append(o)
print(*parent[2:], sep='\n')