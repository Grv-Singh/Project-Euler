def sum_of_div(n):
    divs = 0
    for i in range(2,int(n/2)+1):
        if n%i==0:
            divs+=i
    return divs

res = 0
j = 1
while j<=10000 and k=sum_of_div(j)<=10000:
    if j==k and sum_of_div(k)==k:
        res = res + j + k
    j+=1