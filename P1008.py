for i in range(123,330):
    a = i
    b = 2*i
    c = 3*i
    a1 = a//100
    a2 = (a%100)//10
    a3 = a%10
    b1 = b//100
    b2 = (b%100)//10
    b3 = b%10
    c1 = c//100
    c2 = (c%100)//10
    c3 = c%10
    if(a1+a2+a3+b1+b2+b3+c1+c2+c3 == 45 and a1*a2*a3*b1*b2*b3*c1*c2*c3==362880):
        print(a,b,c)