import sys
n, k = map(int, sys.stdin.readline().split())

count = 1
while k > n:
    if k==n:
        break
    if k%2==0:
        k = k//2
        count+=1
    else:
        if k%10 == 1:
            k = (k-1)//10
            count+=1
        else:
            count = -1
            break
print(count)
