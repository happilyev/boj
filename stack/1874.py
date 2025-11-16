
n = int(input())
goal_seq = [int(input()) for _ in range(n)]
stack = []

for i in range(1,10):
    if goal_seq[0] == i:
        goal_seq.pop()
        print('-')
    else:
        stack.append(i)
        print('+')




# 12345678

# 12

# 436

