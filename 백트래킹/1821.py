n, f = map(int, input().split())
temp = range(1,n+1)
n_temp = list()
half = len(temp)//2 if len(temp)%2==0 else len(temp)//2+1
for i in range(half+1):
    print(temp[i], temp[i+1])
    n_temp.append(temp[i]+temp[i+1])

print(n_temp)