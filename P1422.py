p = int(input())
if(p<=150):
    print("%.1f" % (p*0.4463))
elif(p<400):
    print("%.1f" % (150*0.4463+0.4663*(p-150)))
else:
    print("%.1f" % (150*0.4463+250*0.4663+0.5663*(p-400)))

#不加float会有can't multiply sequence by non-int of type 'float'的错误
#print("%.1f" % p*0.4463)中会先运算"%.1f" % p 然后再*
