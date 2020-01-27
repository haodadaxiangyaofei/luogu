#使用字典保存所有点的信息
n = int(input())
ground = {}
for i in range(n):
    a,b,g,k = list(map(int,input().split()))
    for x in range(a,a+g+1):
        for y in range(b,b+k+1):
            ground[(x,y)] = i+1
x,y = list(map(int,input().split()))
if((x,y) not in ground):
    print(-1)
else:
    print(ground[(x,y)])

# 0≤n≤10,000  0≤a,b,g,k ≤100,000
#空间O(100,000^2)10^10
#时间O(10,000*100,000^2)10^14