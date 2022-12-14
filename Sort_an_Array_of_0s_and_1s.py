n=int(input())
lst=list(map(int,input().split()))
l=[0]*n
for i in range(n):
    if lst[i]==1:
        l[n-1]=1
        n=n-1
for i in l:
    print(i,end=" ")