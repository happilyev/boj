import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
accum = [0]*(n+1)
accum[0] = 0
for i in range(1,n+1):
    accum[i] = accum[i-1]+arr[i-1]
for _ in range(m):
    i, j = map(int, input().split())
    print(accum[j]-accum[i-1])