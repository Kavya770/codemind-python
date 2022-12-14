num=int(input())
lst=list(map(int,input().split()))
for i in lst:
    l=lst.count(i)
    if l==2:
        print(i)
        break