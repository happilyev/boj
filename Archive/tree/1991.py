import sys
input = sys.stdin.readline

n = int(input())
nodes = {}
for _ in range(n):
    root,left,right = input().strip().split()
    nodes[root] = {}
    nodes[root]['left'] = left.replace('.','')
    nodes[root]['right'] = right.replace('.','')

preorder = ''
def preorder(node):
    if not node:
        return
    print(node, end='')
    preorder(nodes[node]['left'])
    preorder(nodes[node]['right'])
def inorder(node):
    if not node:
        return
    inorder(nodes[node]['left'])
    print(node, end='')
    inorder(nodes[node]['right'])
def postorder(node):
    if not node:
        return
    postorder(nodes[node]['left'])
    postorder(nodes[node]['right'])
    print(node, end='')
preorder('A')
print()
inorder('A')
print()
postorder('A')
