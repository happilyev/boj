x,y = input().split()
dif = len(y)-len(x)

def counts(x,y):
    count = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            count+=1
    return count
diffs = []
for i in range(0,dif+1):
    diffs.append(counts(x,y[i:len(x)+i]))
print(min(diffs))

#def counts(a, b):
#    return sum(1 for i in range(len(a)) if a[i] != b[i])
#print(min(counts(x, y[i:i+len(x)]) for i in range(dif+1)))