n = int(input())
arr = [tuple(map(int,reversed(input().split()))) for _ in range(n)]

arr.sort()
print('\n'.join(f"{y} {x}" for x,y in arr))