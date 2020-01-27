n = int(input())
i = 1
while True:
    if((1+i)*i//2)>=n:
        break
    i += 1
i -= 1
n = n - (i+1)*i//2
a = n
b = i+2-n
if(i%2 == 1):
    print("%d/%d" % (a,b))
else:
    print("%d/%d" % (b,a))