n = int(input())
book = list(map(int,input().split()))
mean = sum(book)//n
book = [i-mean for i in book]
count = 0
for i in range(n-1):
    if(book[i]==0):
        continue
    else:
        count = count+1
        book[i+1]=book[i+1]+book[i]
print(count)