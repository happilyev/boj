import sys
import heapq

input = sys.stdin.readline
v = int(input())
e = int(input())
p = [[] for _ in range(v+1)]
dist = [float('inf')]*(v+1)
path = [[] for i in range(v+1)]
for _ in range(e):
    u, v_, w = map(int, input().split())
    p[u].append((v_,w))

k,f = map(int, input().split())
dist[k] = 0
pq = [(0,k,[k])]
while pq:
    d, node, route = heapq.heappop(pq)
    if d>dist[node]:
        continue
    if node == f:
        break
    for v_,w in p[node]:
        if d+w < dist[v_]:
            dist[v_] = d+w
            path[v_] = route + [v_]
            heapq.heappush(pq, (dist[v_], v_, route + [v_]))
print(dist[f] if dist[f] != float('inf') else "INF")
print(len(path[f]))
print(' '.join(map(str,path[f])))