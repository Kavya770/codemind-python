def primes(num):
    if num==1:
        return False
    for j in range(2,num):
        if num%j==0:
            return False
    else:
        return True
n=int(input())
l=list(map(int,input().split()))
c=0
n1=0
for i in l:
    if primes(i):
        c=c+i
        n1=n1+1
c=c/n1
print("%.2f"%c)