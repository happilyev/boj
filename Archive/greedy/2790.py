import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input().strip()) for _ in range(n)]
arr.sort()
for i in range(len(arr)):
    arr[i] = arr[i]+n
    n-=1
count = 0
max_num = max(arr)
for i in range(len(arr)-1):
    if arr[i] >= max_num:
        count+=1
    n+=1
    arr[i+1] += n
if arr[-1] > max_num:
    print(count+1)
else:
    print(count)