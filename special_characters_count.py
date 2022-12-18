str=input()
c=0
for i in str:
    if i.isalnum():
        continue
    elif i.isdigit():
        continue
    elif i.isspace():
        continue
    else:
        c=c+1
print(c)