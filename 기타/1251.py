import sys
arr = list(map(int,sys.stdin.readlines()))
arr1 = sorted(arr, reverse=True)
accum = 0
solved = []
for i in range(5):
    accum+=arr1[i]
    solved.append(arr.index(arr1[i])+1)
solved.sort()
print(accum)
print(' '.join(list(map(str,solved))))