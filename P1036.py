def isprime(a):
    num = sum(a)
    for i in range(2,int(num ** 0.5)+1):
        if((num % i)==0):
            return 0
    return 1
def subset(n,k,numbers):
    output = []
    for i in range(2 ** n):
        tmp = []
        for j in range(n):
            if(((i>>j)%2)==1):
                tmp.append(numbers[j])
        if(len(tmp)==k):
            output.append(tmp)
    return output
n,k = list(map(int,input().split()))
numbers = list(map(int,input().split()))
sub = subset(n,k,numbers)
res = list(map(isprime,sub))
print(sum(res))