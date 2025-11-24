from itertools import permutations
n, m = map(int,input().split())
seq = permutations(range(1,n+1), m)

for i in seq:
    print(' '.join(map(str,i)))