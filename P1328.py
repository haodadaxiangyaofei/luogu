N,Na,Nb = list(map(int,input().split()))
arraya = list(map(int,input().split()))
arrayb = list(map(int,input().split()))
arrayA = [0]*N
arrayB = [0]*N
for i in range(N):
    arrayA[i] = arraya[i%Na]
    arrayB[i] = arrayb[i%Nb]
counta = 0
countb = 0
book = [[0,0,1,1,0],
        [1,0,0,1,0],
        [0,1,0,0,1],
        [0,0,1,0,1],
        [1,1,0,0,0]]
for i in range(N):
    counta += book[arrayA[i]][arrayB[i]]
    countb += book[arrayB[i]][arrayA[i]]
print(counta,countb)
