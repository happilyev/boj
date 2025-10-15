import sys

input = sys.stdin.readline

n = int(input())
called = [int(input()) for _ in range(n)]
last = called[-1]
total = set(range(1,called[-1]+1))
miss = total-set(called)
if miss:
    print('\n'.join(map(str,sorted(list(miss)))))
else:
    print('good job')
#print('\n'.join(list(map(str,sorted(list(total-set(called)))))))