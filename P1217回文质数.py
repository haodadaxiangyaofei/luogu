book = [True]*10000000
book[0]=False
book[1]=False
for i in range(2,10000000-1):
    if(book[i]==False):
        continue
    else:
        j = i
        while(j<10000000):
            book[j]=False
            j = j+i

#print(book)