import sys
n, k = map(int, sys.stdin.readline().split())
cable = [int(sys.stdin.readline()) for _ in range(n)]

left, right = 1, max(cable)
result = 0
while left <= right:
    mid = (left+right) // 2
    count = sum(x // mid for x in cable)
    if count >= k:
        result = mid
        left = mid + 1
    else:
        right = mid -1

print(result)