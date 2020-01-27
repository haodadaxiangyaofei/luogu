#使用从后往前搜索
n = int(input())
carpets = []
for i in range(n):
    a,b,g,k = list(map(int,input().split()))
    carpets.append([a,b,a+g,b+k])
x,y = list(map(int,input().split()))
flag = 0
for i in range(n-1,-1,-1):
    a,b,c,d = carpets[i]
    if(a<=x<=c and b<=y<=d):
        print(i+1)
        flag = 1
        break
if(flag == 0):
    print(-1)
# 0≤n≤10,000  0≤a,b,g,k ≤100,000
#空间O(10,000)
#时间O(10,000)