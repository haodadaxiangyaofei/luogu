'''
@Author: Haodada
@Date: 2019-12-13 08:50:57
@LastEditTime: 2019-12-13 08:59:00
@Description: file content
'''
flag = 1
A,B,C = list(map(int,input().split()))
for i in range(100,1000):
    a = i
    b = i/A*B
    c = i/A*C
    a1 = a//100
    a2 = (a%100)//10
    a3 = a%10
    b1 = b//100
    b2 = (b%100)//10
    b3 = b%10
    c1 = c//100
    c2 = (c%100)//10
    c3 = c%10
    if(a1+a2+a3+b1+b2+b3+c1+c2+c3 == 45 and a1*a2*a3*b1*b2*b3*c1*c2*c3==362880):
        print(a,int(b),int(c))
        flag = 0
if(flag==1):
    print("No!!!")
