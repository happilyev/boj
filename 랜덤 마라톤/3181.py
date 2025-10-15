ban = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
words = input().split()
result = ""
for i in range(len(words)):
    if words[i] in ban and i!=0:
        pass
    else:
        result+=words[i][0].upper()
print(result)