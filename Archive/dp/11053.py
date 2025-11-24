n = int(input())
seq = list(map(int,input().split()))
dp = [1]*n

for i in range(1,len(seq)):
    for o in range(i):
        if seq[i] > seq[o]:
            dp[i] = max(dp[i],dp[o]+1)
print(max(dp))