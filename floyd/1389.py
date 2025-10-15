import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
adj = [[sys.maxsize for j in range(n+1)] for _ in range(n+1)]

for i in range(n):
    adj[i+1][i+1]=0
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[a][b]=1
    adj[b][a]=1

for k in range(1,n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            adj[i][j] = min(adj[i][j], adj[i][k]+adj[k][j])

min = sys.maxsize
bacon = None
for i in range(1,n+1):
    dist = 0
    for j in range(1,n+1):
        dist+=adj[i][j]
    if min > dist:
        min = dist
        bacon = i
print(bacon)