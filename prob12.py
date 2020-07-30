import math

def prime(x):
    flag = True
    for i in range(2,int(x/2)):
        if x%i==0:
            flag = False
            break
    return flag

i=3
while 1:
    i+=1
    sum=(i*(i+1))/2
    c=0
    if not prime(sum):
        for j in range(2,int(math.sqrt(sum))+1):
            if c>500:
                print(sum)
                break
            else:
                if sum%j==0:
                    c+=1
                else:
                    continue
