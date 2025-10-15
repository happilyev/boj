import sys
n, k = map(int, sys.stdin.readline().split())
a = [int(sys.stdin.readline()) for _ in range(n)]
a.reverse()
acc = 0
count = 0
for i in range(n):
    if acc == k:
        break
    if a[i]<=k-acc:
        count += (k-acc)//a[i]
        acc += (k-acc)//a[i] * a[i]
print(count)