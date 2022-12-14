n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in lst:
    if lst.count(i)==1:
        l.append(i)
if len(l)>0:
    for i in l:
        print(i,end=" ")
else:
    print(-1)