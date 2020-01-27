'''
@Author: Haodada
@Date: 2019-12-11 20:54:09
@LastEditTime: 2019-12-11 21:11:10
@Description: file content
'''
def cov(a):
    b=[]
    for i in range(len(list(a))):
        b.append(a[len(a)-1-i])
    return "".join(b)
string = input()
if("." in string):
    a,b = string.split(".")
    a = cov(a)
    b = str(int(b))
    b = cov(b)
    print(str(int(a))+"."+b)
elif("/" in string):
    a,b = string.split("/")
    a = cov(a)
    b = cov(b)
    print(str(int(a))+"/"+str(int(b)))
elif("%" in string):
    a = string.split("%")[0]
    a = cov(a)
    print(str(int(a))+"%")
else:
    print(str(int(cov(string))))
    