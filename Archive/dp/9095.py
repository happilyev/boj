import sys
n = int(sys.stdin.readline())
test_case = [int(sys.stdin.readline()) for _ in range(n)]

dp = [0] * (max(test_case) + 1)
dp[0] = 1

for i in range(1, len(dp)):
    for o in [1,2,3]:
        if i - o >= 0:
            dp[i] += dp[i-o]
for t in test_case:
    print(dp[t])