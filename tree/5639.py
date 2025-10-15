import sys
sys.setrecursionlimit(10**6)
input = sys.stdin
inputs = [int(i.strip()) for i in input]

tree = {}
tree[inputs[0]] = {'left':None,'right':None}

root = inputs[0]

def postorder(start, end):
    if start >= end:
        return
    root = inputs[start]
    idx = start + 1
    while idx < end and inputs[idx] < root:
        idx += 1
    postorder(start+1, idx)
    postorder(idx, end)
    print(root)
postorder(0, len(inputs))