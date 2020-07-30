j=1
count=0
while 1:
    i=j
    for c in range(1,17):
        if i%2!=0:
            i=(i*3)+1
        else:
            i=i/2
        if i==1:
            if c==16:
                count=count+1
                print(j)
                print(count)
            break
    j=j+1
