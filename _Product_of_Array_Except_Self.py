n=int(input())
lst=list(map(int,input().split()))
for j in range(n):
    p=1
    for i in range(n):
        if i!=j:
            p=p*lst[i]
    print(p,end=" ")