n = int(input())
x = [64]
while True:
    if n == 64:
        break
    x.sort()
    x.insert(1, x[0]//2)
    x[0] = x[0]//2
    if x[0] > n:
        del x[1]
    elif x[0] == n:
        break
    if x[0]==1:
        break
result = x[-1]
count = 1
for i in range(len(x)-2,0,-1):
    if result+x[i] > n:
        continue
    else:
        result+=x[i]
        count+=1
print(count)