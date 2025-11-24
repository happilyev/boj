import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    string = input()
    opened = 0
    vps = True
    for i in string:
        if i == '(':
            opened+=1
        elif i == ')':
            if opened != 0:
                opened-=1
            else:
                vps = False
                break
    if vps == True and opened == 0:
        print('YES')
    else:
        print("NO")
        