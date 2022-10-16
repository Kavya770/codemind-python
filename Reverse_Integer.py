n=int(input())
m=n
if n<0:
    n=n*-1
rev=0
while n:
    d=n%10
    rev=rev*10+d
    n=n//10
if(m<0):
    print(rev*-1)
else:
    print(rev)