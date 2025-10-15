from itertools import combinations_with_replacement
n, m = map(int,input().split())
seq = combinations_with_replacement(range(1, n+1), m)

for i in seq:
    print(' '.join(map(str,list(i))))