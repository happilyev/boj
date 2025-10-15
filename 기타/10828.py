import sys
input = sys.stdin.readline

n = int(input())
stack = list()
for _ in range(n):
    cmd = input().strip()
    if cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        print(1 if len(stack)==0 else 0)
    elif cmd == 'top':
        print(-1 if len(stack)==0 else stack[-1])
    elif  cmd == 'pop':
        print(-1 if len(stack)==0 else stack.pop())
    elif 'push' in cmd:
        stack.append(int(cmd.split()[1]))