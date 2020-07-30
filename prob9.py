import math

a=0
b=0
c=1
while 1:
    for b in range(a,c):
        for a in range(0,b):
            if a!=0 and b!=0:
                if (math.sqrt(math.pow(a,2)+math.pow(b,2))).is_integer():
                    if (a+b+int(math.sqrt(math.pow(a,2)+math.pow(b,2))))==1000:
                        print(a*b*int(math.sqrt(math.pow(a,2)+math.pow(b,2))))
    c+=1
