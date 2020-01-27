'''
@Author: Haodada
@Date: 2019-12-13 09:00:11
@LastEditTime: 2019-12-13 09:08:08
@Description: file content
'''
n,s = list(map(int,input().split()))
a,b = list(map(int,input().split()))
apples = []
for i in range(n):
    apple = list(map(int,input().split()))
    if(apple[0]<=a+b):
        apples.append(apple)
apples.sort(key=lambda x: x[1])
count = 0
for apple in apples:
    if(s>=apple[1]):
        count += 1
        s = s - apple[1]
print(count)