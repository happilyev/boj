from itertools import product as func
n, m = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()
seq = func(arr, repeat=m)
for i in seq:
    print(' '.join(map(str,i)))