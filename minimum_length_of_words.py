str=input()
l=str.split()
min=len(str)
for i in l:
    if len(i)<min:
        min=len(i)
print(min)