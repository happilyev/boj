import sys
input = sys.stdin.readline

n = int(input().rstrip())
cards = list(map(int, input().split()))
score = 0
prev = None
for x in cards:
    if prev is None:
        score += x
    else:
        if x - prev != 1:
            score += x
    prev = x

print(score)

