str=input()
s=input()
vowels="AEIOUaeiou"
for i in str:
    if s==i and i in vowels:
        print("True")
        print(str.index(i))
        break
else:
    print("False")