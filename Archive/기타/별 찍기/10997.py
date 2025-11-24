import sys
input = sys.stdin.readline

n = int(input().strip())
w = n*4-3
h = 4*n-1
board = [[' ' for _ in range(w)] for _ in range(h)]

def tri(r, c, width, height):
    for x in range(width): board[r][c-x] = '*'
    c = w-width
    for x in range(1,height): board[x+r][c] = '*'
    r = height-1
    if c == w//2: # r은 세로 c는 가로
        return
    for x in range(width): board[r][x] = '*'
    c = width-1
    for x in range(r,h-height+1,-1): board[x][c] = '*'
    r = h-height+2
    width -= 2
    height -= 4
    tri(r, c, width, height)

if n == 1:
    print('*')
else:
    tri(0, w-1, w, h)
    for i in board:
        print(''.join(i))
