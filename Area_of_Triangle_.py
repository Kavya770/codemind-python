a,b,c=map(int,input().split())
s=(a+b+c)/2
a=s*(s-a)*(s-b)*(s-c)
area=a**(1/2)
print("%.2f"%area)