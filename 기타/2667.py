# import sys
# from collections import deque

# input = sys.stdin.readline


# n = int(input())
# board = [list(map(int, input().strip())) for _ in range(n)]
# visited = [[False]*n for _ in range(n)]

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# def bfs(x, y, visited):
#     queue = deque([(x, y)])
#     visited[x][y] = True
#     while queue:
#         cx, cy = queue.popleft()
#         for i in range(4):
#             nx, ny = cx + dx[i], cy + dy[i]
#             if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
#                 if board[nx][ny] == 1:
#                     visited[nx][ny] = True
#                     queue.append((nx,ny))

# def count_regions():
#     visited = [[False]*n for _ in range(n)]
#     sizes = []
#     for i in range(n):
#         for j in range(n):
#             if not visited[i][j] and board[i][j] == 1:
#                 sizes.append(bfs(i, j, visited))
#     return sizes

# normal = count_regions()

# print(len(normal))
# for i in sorted(normal):
#     print(i)


import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    size = 1
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and board[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    size += 1
    return size

def count_regions():
    sizes = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] == 1:
                sizes.append(bfs(i, j))
    return sizes

sizes = count_regions()
print(len(sizes))
for s in sorted(sizes):
    print(s)
