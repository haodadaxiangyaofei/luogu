x,n = list(map(int,input().split()))
a = n//7
b = n%7
if(x+b-1<6):
    m = a*250*5+b*250
elif(x+b-1<7 and x<=5):
    m = a*250*5+(b-1)*250
elif(x+b-1>=7 and x<=5):
    m = a*250*5+(b-2)*250
elif(x==6 and b<=2):
    m = a*250*5
elif(x==6 and b>2):
    m = a*250*5+(b-2)*250
elif(x==7 and b<=1):
    m = a*250*5
else:
    m = a*250*5+(b-1)*250
print(m)
