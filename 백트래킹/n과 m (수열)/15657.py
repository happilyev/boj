from itertools import combinations_with_replacement as func
n, m = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()
seq = func(arr, m)
for i in seq:
    print(' '.join(map(str,i)))