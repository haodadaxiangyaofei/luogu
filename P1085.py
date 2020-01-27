max = 0
temp = 0
for i in range(7):
    a,b = list(map(int,input().split()))
    if(a+b>temp):
        temp = a+b
        max = i+1
if(temp>8):
    print(max)
else:
    print(0)