n=int(input())
lst=list(map(int,input().split()))
max=0
for i in lst:
    l=len(str(abs(i)))
    if l>max:
        max=l
c=0
for i in lst:
    l=len(str(abs(i)))
    if l==max:
        c=c+1
print(c)