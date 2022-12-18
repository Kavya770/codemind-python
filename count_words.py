str=input()
s=str.split()
c=0
vowels="AEIOUaeiou"
consonants="bcdefghjklmnpqrstvwxyzBCDEFGHJKLMNPQRSTVWXYZ"
for i in s:
    if i[0] in vowels and i[-1] in consonants:
        c=c+1
print(c)