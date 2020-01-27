n = int(input())
fish = list(map(int,input().split()))
lover = []
for i in range(n):
    love = fish[i]
    count = 0
    for j in range(i):
        if(fish[j]<love):
            count = count+1
    lover.append(count)
for f in lover:
    print(f,end=" ")