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
for i in range(m,n+1):
    if prime(i):
        print(i)