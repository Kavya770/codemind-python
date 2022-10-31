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
c=0
for i in range(1,n+1):
    if n%i==0 and prime(i)==False:
        c+=1
print(c)