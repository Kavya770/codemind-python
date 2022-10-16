n=int(input())
s=0
m=1
print(s,m,end=" ")
for i in range(n-2):
    next=s+m
    s=m
    m=next
    print(next,end=" ")