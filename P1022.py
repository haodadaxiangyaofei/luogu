string = input()
for i in range(26):
    ch = chr(i+ord('a'))
    if(ch in string):
        string = string.replace(ch,"j")
        break
string = string.replace("=","-(")+")"
c = eval(string,{"j":1j})
print(ch+"=%.3f" % float(-c.real/c.imag))
# def read(i):#返回系数、是否是x前的系数、该项所占字符数
#     if(string[i]=="a"):
#         return 1,1,1
#     if(string[i]!="+" and string[i]!="-"):
#         num = []
#         count = 0
#         while( i<=len(string)-1):
#             if(string[i]=="+" or string[i]=="-" or string[i]=="a"):
#                 break
#             num.append(string[i])
#             i = i+1
#             count += 1
#         a = int("".join(num))
#         if(i<= len(string)-1 and string[i]=="a"):
#             b = 1
#             count+=1
#         else:
#             b = 0
#         return a,b,count
#     else:
#         if(string[i]=="+"):
#             i+=1
#             while(string[i]!="+" and string[i]!="-" and string[i]!="a"):
#                 num.append(string[i])
#                 i = i+1
#                 count += 1
#             a = int("".join(num))
#             if(string[i]=="a"):
#                 b = 1
#                 count+=1
#             else:
#                 b = 0
#             return a,b,count
#         else:
#             i+=1
#             while(string[i]!="+" and string[i]!="-" and string[i]!="a"):
#                 num.append(string[i])
#                 i = i+1
#                 count += 1
#             a = int("".join(num))
#             if(string[i]=="a"):
#                 b = 1
#                 count+=1
#             else:
#                 b = 0
#             return -a,b,count

        

        
    



# string = input()
# for i in range(26):
#     ch = chr(i+ord('a'))
#     string.replace(ch,"a")
# eqleft = 1
# x = 0
# c = 0
# i=0
# while i <= len(string)-1:
#     if(string[i] == "="):
#         eqleft = 0
#         i += 1
#         continue
#     if(eqleft == 1):
#         a,b,l = read(i)
#         i += l
#         if(b ==1):
#             x += a
#         else:
#             c += a
#     else:
#         a,b,l = read(i)
#         i += l
#         if(b ==1):
#             x -= a
#         else:
#             c -= a
# print(c,x)
# print("%.3f" % (-c/x))


   

