import sys

input = sys.stdin.readline

n, k = map(int, input().strip().split())

data = {}
for _ in range(n):
    w, v = map(int,input().strip().split())
    data[n] = k