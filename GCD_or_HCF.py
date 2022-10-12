n,m=map(int,input().split())
while m:
    if n>m:
        n,m=m,n
    m=m%n
print(n)
    