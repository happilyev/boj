import sys
n = int(sys.stdin.readline())
arr = []
obj = {}
for i in range(n):
    data = int(sys.stdin.readline())
    arr.append(data)
    if data not in obj:
        obj[data] = 1
    else:
        obj[data]+=1
print(round(sum(arr)/n))
print(sorted(arr)[n//2])
max_val = max(obj.values())
max_data = [a for a,b in obj.items() if b==max_val]
max_data.sort()
print(max_data[0] if len(max_data)==1 else max_data[1])
print(max(arr)-min(arr))