import sys
n, k = map(int, sys.stdin.readline().split())

is_prime = [True] * (n+1)
count = 0

for i in range(2, n+1):
    if is_prime[i]:
        for o in range(i, n+1, i):
            if is_prime[o]:
                is_prime[o] = False
                count+=1
                if count == k:
                    print(o)




