n = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))
dp = [0]*100

for i in range(len(L)):
    for o in range(99, L[i]-1, -1):
        dp[o] = max(dp[o], dp[o-L[i]]+J[i])
print(dp[-1])