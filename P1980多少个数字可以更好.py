n,x = list(map(int,input().split()))
count = [0]*10
temp = n
for i in range(1,n+1):
    temp = i
    while(temp!=0):
        count[temp % 10] = count[temp % 10]+1
        temp = temp//10
print(count)
#暴力O(nlogn)

#转为字符串调用count函数O(n)?
l=[]
for i in range(1,n+1):
    l.extend(list(str(i)))
print(l.count(str(x)))

