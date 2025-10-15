import sys
input = sys.stdin.readline

n = input()
a = [list(map(int,input().strip().split())) for _ in range(3)]

if 7 in a[0] and 7 in a[1] and 7 in a[2]:
    print(777)
else:
    print(0)