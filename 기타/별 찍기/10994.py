import sys
input = sys.stdin.readline

n = int(input().strip())
w = 4*n - 3
board = [[' ' for _ in range(w)] for _ in range(w)]

def tri(r, c, width):
    if width == 1:
        board[r][c] = '*'
        return
    for x in range(c,c+width): board[r][x] = '*'
    for x in range(r,r+width): board[x][c] = '*'
    for x in range(r,r+width): board[x][c+width-1] = '*'
    for x in range(c,c+width): board[r+width-1][x] = '*'
    width = width - 4
    tri(r+2, c+2, width)

if n == 1:
    print('*')
else:
    tri(0, 0, w)
    for i in board:
        print(''.join(i))
