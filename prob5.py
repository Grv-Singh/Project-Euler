i=20
j=20
while 1:
    if j==2:
        break
    if i%j==0:
        j-=1
        continue
    else:
        j=20
    i+=1
print(i)
