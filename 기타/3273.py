import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())
arr.sort()
s, e, count = 0, n-1, 0
while s < e:
    if arr[s]+arr[e] == x:
        count+=1
        s+=1
        e-=1
    elif arr[s]+arr[e] < x:
        s+=1
    else:
        e-=1
print(count)