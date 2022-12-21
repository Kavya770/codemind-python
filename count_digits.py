n=int(input())
lst=list(map(int,input().split()))
for i in lst:
    l=len(str(abs(i)))
    print(l,end=" ")