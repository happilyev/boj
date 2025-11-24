import sys

n = int(sys.stdin.readline())
times = map(int, sys.stdin.readline().split())
acc = 0
result = 0
for i in sorted(times):
    acc+=i
    result+=acc
print(result)

####################################################

n = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split()))

acc = 0
result = 0
used = [False] * n

for _ in range(n):
    min_time = float('inf')
    idx = -1
    for i in range(n):
        if not used[i] and times[i] < min_time:
            min_time = times[i]
            idx = i
    used[idx] = True

    acc += min_time
    result += acc

print(result)