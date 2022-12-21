n=int(input())
lst=list(map(int,input().split()))
max=0
for i in lst:
    l=len(str(abs(i)))
    if l>max:
        max=l
l1=[]
for i in lst:
    l=len(str(abs(i)))
    if l==max:
        if i not in l1:
            print(i,end=" ")
            l1.append(i)
