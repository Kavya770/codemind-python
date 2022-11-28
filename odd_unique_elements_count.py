n=int(input())
l=list(map(int,input().split()))
lst=[]
for i in l:
    if i not in lst and i%2:
        lst.append(i)
print(len(lst))