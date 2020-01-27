L,M = list(map(int,input().split()))
road = [1]*(L+1)
for i in range(M):
    start,end = list(map(int,input().split()))
    for j in range(start,end+1):
        road[j]=0
print(sum(road))