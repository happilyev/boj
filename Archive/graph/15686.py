import sys
input = sys.stdin.readline

n, m = map(int,input().split())
house = []
chicken = []
for r in range(1,n+1):
    temp = input().strip().split()
    for c in range(1,len(temp)+1):
        if temp[c-1]=='1':
            house.append((r,c))
        elif temp[c-1]=='2':
            chicken.append((r,c))
dist = [[] for _ in range(len(house))]
for i in range(len(house)):
    for j in range(len(chicken)):
        length = abs(chicken[j][0]-house[i][0]) + abs(chicken[j][1]-house[i][1])
        dist[i].append((chicken[j],length))
print(dist)




