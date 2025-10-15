a, b, v = map(int, input().split())
print(((v-a)//abs(b-a) if (v-a)%abs(b-a)==0 else (v-a)//abs(b-a)+1) +1)
# while True:
#     (v-a)//(b-a)+1
#     l+=a
#     d+=1
#     if l>=v:
#         break
#     l-=b
# print(d)