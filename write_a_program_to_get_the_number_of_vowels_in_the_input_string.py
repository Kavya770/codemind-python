str=input()
vowels="AEIOUaeiou"
count=0
for i in str:
    if i in vowels:
        count+=1
print(count)