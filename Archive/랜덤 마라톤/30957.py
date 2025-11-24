n = int(input().strip())
s = input().strip()

cntB = cntS = cntA = 0

for c in s:
    if c == 'B':
        cntB += 1
    elif c == 'S':
        cntS += 1
    elif c == 'A':
        cntA += 1

if cntB == cntS == cntA:
    print("SCU")
else:
    m = max(cntB, cntS, cntA)
    result = ""
    if cntB == m:
        result += "B"
    if cntS == m:
        result += "S"
    if cntA == m:
        result += "A"
    print(result)
