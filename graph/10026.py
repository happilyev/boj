import sys
from collections import deque

input = sys.stdin.readline


n = int(input())
board = [list(input().strip()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x, y, color, visited, is_color_weak):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if is_color_weak:
                    if (board[nx][ny] in ['R', 'G'] and color in ['R', 'G']) or board[nx][ny] == color:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                else:
                    if board[nx][ny] == color:
                        visited[nx][ny] = True
                        queue.append((nx,ny))

def count_regions(is_color_weak):
    visited = [[False]*n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, board[i][j], visited, is_color_weak)
                count += 1
    return count
normal = count_regions(False)
color_weak = count_regions(True)

print(normal, color_weak)