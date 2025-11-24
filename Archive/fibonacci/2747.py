n = int(input())
a = [0, 1]
while len(a) < n+1:
    a.append(a[len(a)-2]+a[len(a)-1])
print(a[-1])