import sys
input = sys.stdin.readline

n = int(input().strip())
w = 2*n-1
board = [[' ' for _ in range(w*2-1)] for _ in range(w)]



for x in range(n): board[0][x] = board[0][n+(2*n-3)+x] = board[w-1][x] = board[w-1][n+(2*n-3)+x] ='*'
for i in range(1,w-1):
    if i <= w//2:
        board[i][i] = board[i][i+n-1] = board[i][n+(2*n-3)-i] = board[i][n+(2*n-3)-i +n-1] = '*'
    else:
        board[i][w-1-i] = board[i][n*3-i-3] = board[i][n+(2*n-3)+i-(n*2)+2] = board[i][n+(2*n-3)+i-n+1] = '*' #board[i][w*2-1 - (w-1-i)-1]

for i in board:
    print(''.join(i).rstrip())
