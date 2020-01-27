n = int(input())
array = list(map(int,input().split()))
string = ""
for i in range(n+1):
    if(i==0):
        if(array[i]==0):
            continue
        elif(array[i]==-1):
            string += "-"
        elif(array[i]==1):
            a=1
        else:
            string += str(array[i])
    elif(i<n):
        if(array[i]>0):
            string += "+"
            if(array[i]!=1):
                string += str(array[i])
        elif(array[i]<0):
            if(array[i]==-1):
                string += "-"
            else:
                string += str(array[i])
        else:
            continue
    else:
        if(array[i]>0):
            string += "+"
            string += str(array[i])
        elif(array[i]<0):
            string += str(array[i])
        continue
    
    if(n-i!=1):
        string += "x^"
        string += str(n-i)
    else:
        string += "x"
print(string)
