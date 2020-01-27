#动态规划
#只存储一行数据
def take(x,y,a,b):
    if(x==a and y == b):
        return 1
    if((x==a+1 or x==a-1) and (y==b+2 or y==b-2)):
        return 1
    if((x==a+2 or x==a-2) and (y==b+1 or y==b-1)):
        return 1
    return 0

x,y,a,b = list(map(int,input().split()))
table = [0]*(x+1)
temp = [0]*(x+1)
table[0]=1
for i in range(y+1):
    if(take(0,i,a,b)==1):
        temp[0] = 0
    else:
        temp[0] = table[0]
    for j in range(1,x+1):
        if(take(j,i,a,b)==1):
            temp[j] = 0
        else:
            temp[j] = table[j] + temp[j-1]
    table = temp.copy()
print(table[-1])
#时间O(x*y)
#空间O(x)