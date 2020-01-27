n = int(input())
array = list(map(int,input().split()))
count = 0
for k in range(n):
    a = array[k]
    for i in range(n):
        flag = 0
        for j in range(n):
            if (i==j):
                continue
            if((array[i]+array[j])==a):
                count = count + 1
                flag = 1
                break
        if(flag==1):
            break
print(count)