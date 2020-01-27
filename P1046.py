apple = list(map(int,input().split()))
hand = int(input())
hand = hand + 30
count = 0
for x in apple:
    if(x<=hand):
        count = count+1
print(count)