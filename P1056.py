M,N,K,L,D = list(map(int,input().split()))
sm = [0]*(M+1)
sn = [0]*(N+1)
for i in range(D):
    x1,y1,x2,y2 = list(map(int,input().split()))
    if(x1 == x2):
        if(y1 < y2):
            sn[y1]+=1
        else:
            sn[y2]+=1
    else:
        if(x1 < x2):
            sm[x1]+=1
        else:
            sm[x2]+=1
sM = []
for i in range(M):
    sM.append([sm[i],i])
sN = []
for i in range(N):
    sN.append([sn[i],i])
sM.sort(key=lambda x: x[0],reverse=True)
sN.sort(key=lambda x: x[0],reverse=True)
outm = []
for i in range(K):
    outm.append(sM[i][1])
outn = []
for i in range(L):
    outn.append(sN[i][1])
outm.sort()
outn.sort()
for i in range(K):
    print(outm[i],end=' ')
print("")
for i in range(L):
    print(outn[i],end=' ')