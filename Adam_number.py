def reverse(m):
    rev=0
    while m:
        d=m%10
        rev=rev*10+d
        m=m//10
    return rev
n=int(input())
a=n*n
b=reverse(n)
c=b*b
if(a==reverse(c)):
    print("True")
else:
    print("False")