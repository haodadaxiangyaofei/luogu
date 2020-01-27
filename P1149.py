w = [6,2,5,5,4,5,6,3,7,6]
array = [0]*2000
for i in range(2000):
    j = i
    while(j!=0):
        array[i]=array[i]+w[j%10]
        j = j//10
array[0]=6
n = int(input())
count = 0
for i in range(1000):
    for j in range(1000):
        if((array[i]+array[j]+array[i+j]+4)==n):
            count = count+1
print(count)

# w = [6,2,5,5,4,5,6,3,7,6]
# def choose(n):#返回[x1,x2,re],x为选择的数字，res为剩余的火柴
#     res = []
#     if(n<2):
#         return [0]
#     for i in range(10):#当前选0~9的各种情况
#         if(n>=w[i]):#当前的i能够被选
#             res.append([i,n-w[i]])
#             tmp = choose(n-w[i])
#             for j in tmp:
#                 if(j!=0):
#                     j.insert(0,i)
#                     res.append(j)
#     return res

# n = int(input())
# count = 0
# if(n<=10):
#     print(0)
# else:
#     n = n - 4
#     A = choose(n)
#     for a in A:
#         if(a == 0):
#             continue
#         if(a[-1]<2):
#             continue
#         else:
#             B = choose(a[-1])
#             for b in B:
#                 if(b == 0):
#                     continue
#                 if(b[-1] < 2):
#                     continue
#                 C = choose(b[-1])
#                 for c in C:
#                     if(c == 0):
#                         continue
#                     if(c[-1]!=0):
#                         continue
#                     numa = 0
#                     for i in range(len(a)-1):
#                         numa = a[i] + numa*10
#                     numb = 0
#                     for i in range(len(b)-1):
#                         numb = b[i] + numb*10
#                     numc = 0
#                     for i in range(len(c)-1):
#                         numc = c[i] + numc*10 
#                     if(numc != numa+numb):
#                         continue
#                     else:
#                         count = count+1
# print(count)



