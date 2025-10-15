# import sys
# input = sys.stdin.readline
# n = int(input())
# tri = [list(map(int,input().strip().split())) for _ in range(n)]

# dp = [[] for _ in range(n)]
# dp[0].append((0,tri[0][0]))

# for i in range(n):
#     if i < n-1:
#         for o in range(len(dp[i])):
#             x = dp[i][o][0]
#             if x<n:
#                 value = dp[i][o][1]
#                 v1 = tri[i+1][x]
#                 v2 = tri[i+1][x+1]
#                 dp[i+1].append((x,value+v1))
#                 dp[i+1].append((x+1,value+v2))
# print(max(dp[n-1], key=lambda a:a[1])[1])

import sys
input = sys.stdin.readline
n = int(input())
tri = [list(map(int,input().strip().split())) for _ in range(n)]

dp = [[0]*len(tri[i]) for i in range(n)]
dp[0][0] = tri[0][0]

for i in range(n-1):
    for o in range(len(dp[i])):
        value = dp[i][o]
        dp[i+1][o] = max(dp[i+1][o],value+tri[i+1][o])
        dp[i+1][o+1] = max(dp[i+1][o+1],value+tri[i+1][o+1])
print(max(dp[-1]))

