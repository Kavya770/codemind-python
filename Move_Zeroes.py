n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in lst:
    if i!=0:
        l.append(i)
while len(l)!=n:
    l.append(0)
for i in l:
    print(i,end=" ")