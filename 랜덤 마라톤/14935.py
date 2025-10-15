x = int(input())
prev = int(str(x)[0])*len(str(x))
while True:
    temp = int(str(prev)[0])*len(str(prev))
    if prev == temp:
        print("FA")
        break
    elif temp == 0:
        print("NFA")
        break
    prev = temp