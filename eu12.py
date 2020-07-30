div = 0
j = 1
arr= []
while (div+1)<=500:
    div = 1
    arr = []
    k = int((j*(j+1))/2)
    for i in range(2,int(k/2)+1):
        if k%i==0 and i not in arr:
            arr.append(int(k/i))
            div+=2
    j+=1
print(k)