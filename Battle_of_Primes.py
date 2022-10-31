def prime(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                return False
        else:
            return True
    else:
        return False
m=int(input())
n=int(input())
for i in range(1,1000):
    if(prime(m+n+i)==True):
        print(i)
        break