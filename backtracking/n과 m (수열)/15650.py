from itertools import combinations
n, m = map(int,input().split())
seq = combinations(range(1,n+1), m)

for i in seq:
    print(' '.join(map(str,list(i))))


ans = []
def dfs():
    if len(ans) == m:
        print(' '.join(map(str,ans)))
        return
    for i in range(1,n+1):
        if i not in ans:
            if len(ans) == 0:
                ans.append(i)
                dfs()
                ans.pop()
            else:
                if i>ans[-1]:
                    ans.append(i)
                    dfs()
                    ans.pop()
                    