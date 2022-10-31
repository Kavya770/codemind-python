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
m=n
rev=0
while n:
    d=n%10
    rev=rev*10+d
    n=n//10
if (prime(m)):
    if prime(rev):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")