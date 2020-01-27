n = int(input())
book = [1] * (n + 1)
book[0] = 0
book[1] = 0
for i in range(n+1):
    if(book[i] != 0):
        j = i + i
        while j <= n:
            book[j] = 0
            j += i
book1 = []
for i in range(n+1):
    if(book[i] != 0):
        book1.append(i)
m = len(book1)
flag = 0
for i in range(m):
    for j in range(i, m):
        for k in range(j, m):
            if(book1[i]+book1[j]+book1[k]==n ):
                print(book1[i],book1[j],book1[k])
                flag = 1
                break
        if(flag==1):
            break
    if(flag==1):
        break

