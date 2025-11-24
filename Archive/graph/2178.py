import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1:
                    board[nx][ny] = board[cx][cy]+1
                    queue.append((nx,ny))
bfs(0,0)
print(board[n-1][m-1])
