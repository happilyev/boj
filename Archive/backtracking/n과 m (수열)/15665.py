from itertools import product as func
n, m = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()
seq = list(set(func(arr, repeat=m)))
seq.sort()
for i in seq:
    print(' '.join(map(str,i)))