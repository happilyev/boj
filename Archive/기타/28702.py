a = []
for i in range(3):
    a.append(input())
for i in range(3):
    for o in range(3):
        if str(a[o]).isnumeric()==True:
            if o<2 and str(a[o+1]).isnumeric()==False:
                a[o+1]=int(a[o])+1
            if o>0 and str(a[o-1]).isnumeric()==False:
                a[o-1]=int(a[o])-1
n = int(a[2])+1
if n%3==0 and n%5==0:
    print("FizzBuzz")
elif n%3==0:
    print("Fizz")
elif n%5==0:
    print("Buzz")
else:
    print(n)