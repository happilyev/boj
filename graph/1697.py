import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

visited = [False]*100000
dist = [0] * 100000

def bfs(x):
    queue = deque([x])
    visited[x] = True
    while queue:
        cx = queue.popleft()
        
        for i in range(3):
            dx = [cx-1,cx+1,cx*2]
            if 0<= dx[i] < 100000 and not visited[dx[i]]:
                if dx[i] == m:
                    return dist[cx]
                visited[dx[i]] = True
                dist[dx[i]] = dist[dx[i]]+1
                queue.append(dx[i])
bfs(n)
print(n)
