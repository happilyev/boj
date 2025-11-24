import sys
import heapq

input = sys.stdin.readline
v = int(input())
e = int(input())
p = [[] for _ in range(v+1)]
visit = [False]*(v+1)
dist = [float('inf')]*(v+1)
for _ in range(e):
    u, v_, w = map(int, input().split())
    p[u].append((v_,w))

k,f = map(int, input().split())
dist[k] = 0
pq = [(0,k)]
while pq:
    d, node = heapq.heappop(pq)
    if d>dist[node]:
        continue
    for v_,w in p[node]:
        if d+w < dist[v_]:
            dist[v_] = d+w
            heapq.heappush(pq, (dist[v_], v_))
print(dist[f] if dist[f] != float('inf') else "INF")