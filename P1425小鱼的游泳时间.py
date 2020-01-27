a,b,c,d = list(map(int,input().split()))
e = c - a
if(d>=b):
    f = d - b
else:
    f = d - b + 60
    e = e - 1
print(e,f)