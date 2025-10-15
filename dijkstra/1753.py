import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
p = [[] for _ in range(v+1)]
visit = [False]*(v+1)

dist = [float('inf')]*(v+1)
dist[k] = 0
for _ in range(e):
    u, v_, w = map(int, input().split())
    p[u].append((v_,w))

pq = [(0,k)]
while pq:
    d, node = heapq.heappop(pq)
    if d>dist[node]:
        continue
    for v_,w in p[node]:
        if d+w < dist[v_]:
            dist[v_] = d+w
            heapq.heappush(pq, (dist[v_], v_))
for i in range(1, v+1):
    print(dist[i] if dist[i] != float('inf') else "INF")