
def dg(a):
    count = 1
    if(a==1):
        return 1
    for i in range(1,a//2+1):
        if(i in dic):
            dgi = dic[i]
        else:
            dgi = dg(i)
            dic[i] = dgi
        count = count+dgi
    return count

dic= {}
n = int(input())
print(dg(n))