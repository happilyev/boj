import sys
input = sys.stdin.readline
t = int(input())
for p in range(t):
    n = int(input())
    stickers = [list(map(int,input().strip().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(2)]

    for i in range(n):
        a1 = dp[1][i-1] if i-1>=0 else 0
        a2 = dp[0][i-1] if i-1>=0 else 0
        b = dp[0][i-2] if i-2 >= 0 else 0
        c = dp[1][i-2] if i-2 >= 0 else 0
        dp[0][i] = stickers[0][i] + max(a1, b, c)
        dp[1][i] = stickers[1][i] + max(a2, b, c)
    print(max(max(dp[0]), max(dp[1])))