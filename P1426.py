'''
@Author: Haodada
@Date: 2019-12-13 09:32:34
@LastEditTime: 2019-12-13 09:43:10
@Description: file content
'''
s,x = list(map(int,input().split()))
count = 0
l = 0
p = 7
die = 0
while(l<=s+x):
    if(s-x<=l<=s+x):
        count += 1
        if(count==2):
            die = 1
            break
    l = l + p
    p = p*0.98
if(die==1):
    print("y")
else:
    print("n")