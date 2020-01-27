'''
@Author: Haodada
@Date: 2019-12-09 14:01:20
@LastEditTime: 2019-12-09 14:19:16
@Description: file content
'''
n = int(input())
drop = [0]*n
applesum = 0
for i in range(n):
    apple = list(map(int,input().split()))
    app = 0
    
    for j in range(1,apple[0]+1):
        if(j==1):
            app = apple[j]
        else:
            if(apple[j]<=0):
                app = app + apple[j]
            else:
                if(app != apple[j]):
                    drop[i] = 1
                app = apple[j]
    applesum = applesum + app
droptricount = 0
for i in range(n):
    if(drop[i]==1 and drop[(i+1)%n]==1 and drop[(i+2)%n]==1):
        droptricount = droptricount+1
print(applesum,end = " ")
print(sum(drop),end = " ")
print(droptricount,end = " ")