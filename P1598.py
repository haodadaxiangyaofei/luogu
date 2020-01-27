'''
@Author: Haodada
@Date: 2019-12-12 08:06:11
@LastEditTime: 2019-12-12 08:18:57
@Description: file content
'''
string = ""
for i in range(4):
    string = string+input()
count = [0]*26
for i in range(26):
    count[i] = string.count(chr(i+ord("A")))
maxnum = max(count)
while(maxnum!=0):
    for i in range(26):
        if(i==0):
            if(count[i]==maxnum):
                print("*",end="")
                count[i] = count[i]-1
            else:
                print(" ",end="")
        else:
            if(count[i]==maxnum):
                print(" *",end="")
                count[i]=count[i]-1
            else:
                print("  ",end="")
    print("")
    maxnum = maxnum - 1
for i in range(26):
    if(i==0):
        print(chr(i+65),end="")
    else:
        print(" "+chr(i+65),end="")