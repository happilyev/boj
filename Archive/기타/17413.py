import re
s = input()
part = re.split(r"(<[^>]+>)", s)
part = [p for p in part if p]
result = ""
for i in part:
    a = ""
    if "<" not in i:
        if ' ' not in i:
            a = i[::-1]
        else:
            blank = i.split()
            for o in blank:
                a+=o[::-1]+" "
    if a=="":
        result+=i
    else:
        result+=a.strip()
print(result)