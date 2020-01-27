#十连for既爽又快
n = int(input())
count = 0
for a in range(1,4):
    for b in range(1,4):
        for c in range(1,4):
            for d in range(1,4):
                for e in range(1,4):
                    for f in range(1,4):
                        for g in range(1,4):
                            for h in range(1,4):
                                for i in range(1,4):
                                    for j in range(1,4):
                                        if(a+b+c+d+e+f+g+h+i+j==n):
                                            count += 1
print(count)
for a in range(1,4):
    for b in range(1,4):
        for c in range(1,4):
            for d in range(1,4):
                for e in range(1,4):
                    for f in range(1,4):
                        for g in range(1,4):
                            for h in range(1,4):
                                for i in range(1,4):
                                    for j in range(1,4):
                                        if(a+b+c+d+e+f+g+h+i+j==n):
                                            print(a,b,c,d,e,f,g,h,i,j)