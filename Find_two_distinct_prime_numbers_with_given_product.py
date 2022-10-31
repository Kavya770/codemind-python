def prime(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                return False
        else:
            return True
    else:
        return False
n=int(input())
for i in range(2,n):
    if n%i==0:
        if prime(n//i) and prime(i):
            print( i,n//i)
            break
else:
    print(-1)