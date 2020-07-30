import math

def pali(x):
    while 1:
        l=0
        lenth = int(len(str(x)))
        for i in range(0,int((lenth/2))):
            x=str(x)
            if x[lenth-1-i]!=x[i]:
                x=int(x)
                break
            else:
                x=int(x)
                l+=1
        if l==int(lenth/2):
            for j in range(1,999):
                if x%(999-j)==0:
                    if len(str(int(x/(999-j))))==len(str(int(999-j)))==3:
                        print(str(x/(999-j))+" "+str(999-j)+"\n")
                        return x
        x-=1

print(pali(989723))
    
