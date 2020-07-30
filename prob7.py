arr=[2]
i=3
while 1:
    c=0
    for k in range(0,len(arr)):
        if i%arr[k]==0:
            break
        else:
            c+=1
    if c==len(arr):
        if c==10001:
            print(arr[-1])
            break
        else:
            arr.append(i)        
    i+=1
