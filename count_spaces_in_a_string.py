str=input()
wc=0
for i in str:
    if i.isspace():
        wc=wc+1
print(wc)