n=int(input())
max=0
while n:
    d=n%10
    if(d>max):
        max=d
    n=n//10
print(max)