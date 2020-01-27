'''
@Author: Haodada
@Date: 2019-12-11 20:02:28
@LastEditTime: 2019-12-11 20:18:49
@Description: file content
'''
A = list(input())
count1 = 0
for a in A:
    number = ord(a)-ord("A")+1
    if(count1==0):
        count1=number
    else:
        count1 = count1*number
B = list(input())
count2 = 0
for b in B:
    number = ord(b)-ord("A")+1
    if(count2==0):
        count2 = number
    else:
        count2 = count2*number
if(count2%47)==(count1%47):
    print("GO")
else:
    print("STAY")