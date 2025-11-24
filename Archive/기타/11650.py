n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]

arr.sort()
print('\n'.join(f"{x} {y}" for x,y in arr))