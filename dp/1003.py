import sys


dp = [(1,0),(0,1)]
result = []
for i in range(2, 41):
    zero = dp[i-1][0] + dp[i-2][0]
    one = dp[i-1][1] + dp[i-2][1]
    dp.append((zero,one))

z = int(sys.stdin.readline())
for i in range(z):
    a = int(sys.stdin.readline())
    result.append(dp[a])
for i in result:
    print(i[0],i[1])
10658
55741
