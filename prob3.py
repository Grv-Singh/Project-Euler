n = int(input("The Number?"))
i=1
arr=[]
while 1:
    if n%i==0:
        arr.append(i)
        n=n/i
    if n==1:
        print(arr[-1])
        break
    i+=1
