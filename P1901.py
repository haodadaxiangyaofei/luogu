n = int(input())
a1,b1 = list(map(int,input().split()))
a2,b2 = list(map(int,input().split()))
a3,b3 = list(map(int,input().split()))
if(n%a1==0):
    x1 = ((n//a1))*b1
else:
    x1 = ((n//a1)+1)*b1
if(n%a2==0):
    x2 = ((n//a2))*b2
else:
    x2 = ((n//a2)+1)*b2
if(n%a3==0):
    x3 = ((n//a3))*b3
else:
    x3 = ((n//a3)+1)*b3
print(min([x1,x2,x3]))