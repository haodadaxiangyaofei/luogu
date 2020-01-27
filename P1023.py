expect = int(input())
pricebook = []
price1,number1 = list(map(int,input().split()))
base = price1
pricebook.append((price1,number1))
while 1: 
    price2,number2 = list(map(int,input().split()))
    if(price2==-1 and number2==-1):
        break
    step = (number2-number1)//(price2-price1)
    for p in range(price1+1,price2,1):
        pricebook.append((p,number1+step))
        number1 = number1+step
    price1 = price2
    number1 = number2
    pricebook.append((price1,number1))
step = int(input())
price1 = price1+1
number1 = number1-step
while number1>0:
    pricebook.append((price1,number1))
    price1 = price1+1
    number1 = number1-step
for i in range(10000):
    if(pricebook[i][0]==expect):
        expectind = i
        break
flag = 0
for i in range(0,1000,1):
    maxp = max(p[1]*(p[0]-base+i) for p in pricebook)
    p = pricebook[expectind]
    if(maxp == (p[1]*(p[0]-base+i))):
        print(i)
        flag = 1
        break
    maxp = max(p[1]*(p[0]-base-i) for p in pricebook)
    #print(maxp)
    p = pricebook[expectind]
    #print(p[1]*(p[0]-base-i))
    if(maxp == (p[1]*(p[0]-base-i))):
        print(-i)
        flag = 1
        break
if(flag==0):
    print("NO SOLUTION")

    

