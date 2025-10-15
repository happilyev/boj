n = int(input())
r = 0
start = max(1, n-9*len(str(n)))
for i in range(start, n):
    if i + sum(map(int, str(i))) == n:
        r = i
        break

print(r)
