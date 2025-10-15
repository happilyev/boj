from itertools import permutations
n, m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
seq = permutations(arr, m)

for i in seq:
    print(' '.join(map(str,list(i))))