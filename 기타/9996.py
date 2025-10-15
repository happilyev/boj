import sys
input = sys.stdin.readline

n = int(input())
pattern = input().strip()
name = [input().strip() for _ in range(n)]
a, b = map(str, pattern.split("*"))
for i in name:
    if len(i) >= len(a)+len(b) and i.startswith(a) and i.endswith(b):
        print("DA")
    else:
        print("NE")