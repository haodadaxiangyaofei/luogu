n = int(input())
array = list(map(int,input().split()))
max = 0

count = 1
yestoday = 1000000000
for i in range(n):
    if(array[i]<yestoday):
        if(count>max):
            max = count
        count = 1
        yestoday = array[i]
        i = i+1
    else:
        yestoday = array[i]
        i = i+1
        count = count+1

if(count>max):
    max = count
print(max)
