n=int(input())
l=list(map(int,input().split()))
if n%2:
    l.insert((n+1)//2,0)
for i in range((n+1)//2):
    print(l[i],l[-(i+1)],end=" ")