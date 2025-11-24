n = int(input())
stack = []
cur = 1
result = []
able = True
for i in range(n):
    num = int(input())
    while cur<=num:
        stack.append(cur)
        cur+=1
        result.append('+')
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        able=False
        break
if able == True:
    print('\n'.join(result))
else:
    print('NO')
