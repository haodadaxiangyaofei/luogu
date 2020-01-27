from functools import cmp_to_key

a=[(2,4),(2,5),(0,3),(1,3),(0,4)]
def mycmp(x,y):
    if x[0]<y[0]:
        return -1
    if x[0]>y[0]:
        return 1
    if x[0]==y[0]:
        if x[1]==y[1]:
            return 0
        elif x[1]<y[1]:
            return 1
        else:
            return -1

a.sort(key=cmp_to_key(mycmp))
print(a)