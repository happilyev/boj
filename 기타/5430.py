import sys
from collections import deque
import json
input = sys.stdin.readline

t = int(input())
for i in range(t):
    p = input()
    n = int(input())
    rev = False
    dq = deque()
    err = False
    [dq.append(i) for i in (json.loads(input()))]
    for i in p:
        if i=="R":
            rev = True if rev==False else False
        if i=="D":
            if len(dq)==0:
                err = True
                break
            else:
                if rev == True:
                    dq.pop()
                else:
                    dq.popleft()
    if rev == True: dq.reverse()
    if not err: 
        print(json.dumps(list(dq)).replace(' ',''))
    else: print('error')


# import sys
# import json
# input = sys.stdin.readline

# t = int(input())
# for i in range(t):
#     p = input()
#     n = int(input())
#     rev = False
#     arr = json.loads(input())
#     for i in p:
#         if i=="R":
#             rev = True if rev==False else False
#         if i=="D":
#             if len(arr)==0:
#                 print('error')
#                 break
#             else:
#                 if rev == True:
#                     del arr[-1]
#                 else:
#                     del arr[0]
#     if rev == True: arr.reverse()
#     if len(arr)!=0: print(json.dumps(arr, ).replace(' ',''))