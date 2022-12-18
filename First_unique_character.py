str=input()
s=list(str.lower())
l=[]
for i in s:
    L=s.count(i)
    if L==1:
        l.append(i)
if len(l)>0:
    print(l[0])
else:
    print(-1)