str=input()
s=list(str.lower())
l=[]
for i in s:
    if i not in l and i!=" ":
        l.append(i)
l.sort()
str1="".join(l)
print(str1)