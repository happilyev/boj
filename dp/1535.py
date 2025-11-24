import sys
input = sys.stdin.readline
n = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

hp = [0]*100


for i in range(len(L)):
    for o in range(99, L[i]-1, -1):
        hp[o] = max(hp[o],hp[o-L[i]]+J[i])
print(hp[-1])