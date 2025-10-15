import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

adj = [[sys.maxsize for j in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    adj[i][i]=0
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    adj[a][b]= min(adj[a][b], c)

for k in range(1,n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            adj[i][j] = min(adj[i][j], adj[i][k]+adj[k][j])


for i in range(1,n+1):
    for j in range(1,n+1):
        if adj[i][j] == sys.maxsize:
            print(0, end=' ')
        else:
            print(adj[i][j], end=' ')
    print()