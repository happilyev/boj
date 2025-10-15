def gcd(x,y):
    while y!=0:
        x, y = y, x%y
    return x

a, b = map(int,input().split())
c, d = map(int,input().split())
nume = a*d + b*c
deno = b*d
euclid = gcd(nume, deno)
print(nume//euclid, deno//euclid)

        