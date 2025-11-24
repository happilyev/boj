import sys
n, k = map(int, sys.stdin.readline().split())
a = [int(sys.stdin.readline()) for _ in range(n)]


dp = [float('inf')]*(k+1)
dp[0] = 0
for o in a:
    for i in range(o,k+1):
        dp[i] = min(dp[i-o]+1, dp[i])

if dp[k] == float('inf'):
    print(-1)
else:
    print(dp[k])