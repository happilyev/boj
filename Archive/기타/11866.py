n,k = map(int, input().split())
arr = [i for i in range(1,n+1)]
idx = 0
deleted = []
while arr:
    idx = (idx+k-1) % len(arr)
    deleted.append(arr.pop(idx))

print(f"<{', '.join(map(str,deleted))}>")
