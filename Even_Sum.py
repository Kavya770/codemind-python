n=int(input())
l=list(map(int,input().split()))
even=[i for i in l if i%2==0]
print(sum(even))