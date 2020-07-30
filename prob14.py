i=1
z=0
while i<=1000000:
    j=i
    c=0
    while j!=1:
        if j%2==0:
            j=j/2
        else:
            j=(3*j)+1
        c+=1
    if c>z:
        print(i,c)
        z=c
    i=i+1
