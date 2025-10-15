import sys


bfs = {int(sys.stdin.readline()):0}
while 1 not in bfs:
    for i in bfs.copy():
        if i%3==0:
            if i//3 not in bfs or bfs[i//3] > bfs[i]+1:
                bfs[i//3]=bfs[i]+1
        if i%2==0:
            if i//2 not in bfs or bfs[i//2] > bfs[i]+1:
                bfs[i//2]=bfs[i]+1
        if i-1>0:
            if i-1 not in bfs or bfs[i-1] > bfs[i]+1:
                bfs[i-1]=bfs[i]+1

        del bfs[i]
print(bfs[1])