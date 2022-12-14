n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in lst:
    l.append(i*i)
l.sort()
for i in l:
    print(i,end=" ")