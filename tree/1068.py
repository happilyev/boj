import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n)]
node_input = list(map(int, input().strip().split()))
root = -1

for i in range(n):
    if node_input[i] == -1:
        root = i
    else:
        tree[node_input[i]].append(i)

def delete_node(d_node):
    deleted[d_node] = True
    for j in tree[d_node]:
        delete_node(j)
    tree[d_node] = []
d = int(input())
deleted = [False]*n

if d == root:
    print(0)
else:
    delete_node(d)
    count = 0
    for i in range(n):
        if deleted[i]:
            continue
        is_leaf = True
        for j in tree[i]:
            if not deleted[j]:
                is_leaf = False
                break
        if is_leaf:
            count+=1
    print(count)
