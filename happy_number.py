def happy(m):
    s=0
    while m:
        d=m%10
        s=s+d**2
        m=m//10
    return s
n=int(input())
a=happy(n)
while(a>9):
    a=happy(a)
if(a==1 or a==7):
    print("True")
else:
    print("False")