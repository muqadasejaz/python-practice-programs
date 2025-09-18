#write a program to check whether a given character is a vowel or not


char=input("enter the character: ")

if char in ('a','e','i','o','u','A','E','I','O','U'):
    print(char, " is a vowel")
else:
    print(char, " is not a vowel")