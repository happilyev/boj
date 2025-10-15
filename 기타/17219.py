import sys
input = sys.stdin.readline
n, m = map(int, input().split())
p_w = {}
for _ in range(n):
    a, b = input().split()
    p_w[a] = b
for _ in range(m):
    print(p_w[input().strip()])