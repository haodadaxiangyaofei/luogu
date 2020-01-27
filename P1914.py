n = int(input())
string = input()
output = []
for c in string:
    output.append(chr(((ord(c)-ord("a")+n) % 26) + ord("a")))
print("".join(output))