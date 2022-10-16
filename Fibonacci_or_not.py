n=int(input())
s=0
m=1
for i in range(n-2):
    next=s+m
    s=m
    m=next
    if(n==next):
        print("True")
        break
else:
    print("False")