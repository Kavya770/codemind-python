n=int(input())
l=list(map(int,input().split()))
if len(l)!=n:
    for i in range(n-len(l)):
        l.append(0)
lst=[]
for i in l:
    if i not in lst and i%2:
        lst.append(i)
print(sum(lst))