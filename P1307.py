def cov(n):
    n = abs(int(n))
    n = str(n)
    k = []
    for i in range(len(n)):
        k.append(n[len(n)-1-i])
    return int("".join(k))
n = input()
if(int(n)<0):
    print(-cov(n))
else:
    print(cov(n))