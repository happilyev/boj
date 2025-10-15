from collections import deque
a, k = map(int, input().split())

dq = deque([(a,0)])
visited = set()
visited.add(a)

while dq:
    node, count = dq.popleft()
    if node == k:
        print(count)
        break
    if node+1 <= k and (node+1) not in visited:
        visited.add(node+1)
        dq.append((node+1,count+1))
    if node*2 <= k and (node*2) not in visited:
        visited.add(node*2)
        dq.append((node*2,count+1))
