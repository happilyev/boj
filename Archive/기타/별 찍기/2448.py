import sys
input = sys.stdin.readline

n = int(input().strip())
w = 2*n - 1
board = [[' ' for _ in range(w)] for _ in range(n)]

def tri(r, c, size):
    if size == 3:
        board[r][c] = '*'
        board[r+1][c-1] = board[r+1][c+1] = '*'
        for x in range(c-2, c+3): board[r+2][x] = '*'
        return
    half = size // 2
    tri(r, c, half)
    tri(r+half, c-half, half)
    tri(r+half, c+half, half)

tri(0, n-1, n)

for i in board:
    print(''.join(i))
