input()
a = input()
result = 0
temp = ''
for i in a:
    if i.isnumeric():
        temp += i
    else:
        if temp != '': result += int(temp)
        temp = ''
if temp != '': result += int(temp)
print(result)

#print(sum(map(int, re.sub(r'\D', ' ', input()).split())))
#print(sum(map(int, re.findall(r'\d+', input()))))
