i=1
j=2
k=0
print(i)
print(j)
sum=0
while k<=4000000:
    k=j+i
    print(k)
    if k%2==0:
        sum=sum+k
    i=j
    j=k
print(sum+2)
