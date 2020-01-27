n = int(input())
i = 1
sum = 0
while(1):
    sum = sum + 1/i
    if(sum>n):
        print(i)
        break
    i = i+1