n,m = list(map(int,input().split()))
pos = []
for i in range(n):
    a,b = list(input().split())
    if(a =="0"):
        a = 1
    else:
        a = -1
    pos.append([a,b])
now = 0
for i in range(m):
    dec,num = list(map(int,input().split()))
    if(dec == 0):
        dec = -1
    else:
        dec = 1
    now = now + pos[now%n][0]*dec*num
print(pos[now%n][1])