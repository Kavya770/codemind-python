n=int(input())
lst=list(map(int,input().split()))
lst1=sorted(lst,reverse=True)
if lst==lst1:
    print("yes")
else:
    print("no")