from itertools import product as func
n, m = map(int,input().split())
seq = func(range(1,n+1), repeat=m)

for i in seq:
    print(' '.join(map(str,i)))