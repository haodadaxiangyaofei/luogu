M,N = list(map(int,input().split()))
array = list(map(int,input().split()))
memory = []
count = 0
for word in array:
    if(word not in memory):
        count += 1
        if(len(memory)<=M-1):
            memory.append(word)
        else:
            del(memory[0])
            memory.append(word)
            
print(count)
        