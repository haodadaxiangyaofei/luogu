n = float(input())
sum = 0
i = 1
step = 2
while(1):
    sum = sum + step
    if(sum>=n):
        print(i)
        break
    i = i+1
    step = step*0.98
#存在浮点数精度问题