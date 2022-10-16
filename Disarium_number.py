n=int(input())
m=n
s=0
l=len(str(n))
while n:
    d=n%10
    s=s+d**l
    n=n//10
    l=l-1
if(s==m):
    print("True")
else:
    print("False")