import sys

n = int(sys.stdin.readline())
I = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

I.sort(key=lambda x: (x[1], x[0]))
count = 0
end = 0
for i in I:
    if i[0] >= end:
        end = i[1]
        count+=1

print(count)



# acc = 0
# result = 0
# used = [False] * n

# for _ in range(n):
#     min_time = float('inf')
#     idx = -1
#     for i in range(n):
#         if not used[i] and times[i] < min_time:
#             min_time = times[i]
#             idx = i
#     used[idx] = True

#     acc += min_time
#     result += acc

# print(result)