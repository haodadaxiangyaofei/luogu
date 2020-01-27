X = 0
jinjin = 0
mama = 0
flag = 0
for i in range(12):
    jinjin = jinjin + 300
    p = int(input())
    if(jinjin<p and flag == 0):
        X = i+1
        flag = 1
    jinjin = jinjin - p
    if(jinjin//100>0):
        mama = mama+(jinjin//100)*100
        jinjin = jinjin%100
if(flag==0):
    print(int(jinjin+mama*1.2))
else:
    print(-X)

