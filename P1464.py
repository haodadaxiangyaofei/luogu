def w(a,b,c):
    if(a<=0 or b<=0 or c<=0):
        return 1
    if(a>20 or b>20 or c>20):
        return w(20,20,20)
    if((a,b,c) in dic):
        return dic[(a,b,c)]
    if(a<b<c):
        result = w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
        dic[(a,b,c)] = result
        return result
    else:
        result = w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
        dic[(a,b,c)] = result
        return result
dic = {}
out = []
while True:
    a,b,c = list(map(int,input().split()))
    if(a==b==c==-1):
        break
    else:
        out.append([a,b,c,w(a,b,c)])
for i in out:
    print("w(%d, %d, %d) = %d" % (i[0], i[1], i[2],i[3]))