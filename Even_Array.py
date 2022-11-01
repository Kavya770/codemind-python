n=int(input())
l=list(map(int,input().split()))
s=len(l)
c=0
for i in range(s):
    if l[i]%2==0:
        c=c+1
if s==c:
    print("True")
else:
    print("False")