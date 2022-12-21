n,k=map(int,input().split())
lst=list(map(int,input().split()))
c=0
for i in lst:
    l=list(str(abs(i)))
    #print(l,len(l))
    if len(l)==k:
        c=c+1
print(c)