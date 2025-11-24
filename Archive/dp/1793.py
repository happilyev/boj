import sys

arr = list(map(int,sys.stdin.readlines()))
for n in arr:
    if n != 0:
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2,n+1):
            dp[i] = dp[i-1]+2*dp[i-2]
        print(dp[-1])
    else:
        print(1)