n = int(input())
count = 0
if n < 2023:
    print(0)
else:
    for i in range(2023,n+1):
        it = iter(str(i))
        if all(ch in it for ch in '2023') == True:
            count+=1
    print(count)