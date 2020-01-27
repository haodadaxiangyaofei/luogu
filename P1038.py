'''
@Author: Haodada
@Date: 2019-12-11 20:20:47
@LastEditTime: 2019-12-11 20:51:00
@Description: file content
'''
word = input()
inputstring = input()
string = list(inputstring.split())
count = 0
for i in range(len(string)):
    if(word.lower()==string[i].lower()):
        count = count + 1
if(count==0):
    print(-1)

else:
    inputstring = list(inputstring.lower())
    word = list(word.lower())
    first = 0
    i=0
    while(i<len(inputstring)-1):
        
        flag = 1
        for j in range(len(word)):
            if(inputstring[i+j]!=word[j]):
                flag = 0
                break
        if(inputstring[i+j+1]!=" "):
            flag = 0
        if(flag == 1):
            first = i
            break
        while(inputstring[i]!=" "):
            i = i+1
        i = i+1 
    print(count,end=" ")
    print(first)
