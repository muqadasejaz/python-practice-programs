"write a prograam to find palindrome or not"


query= str(input("enter the string: "))

def palindrome(s):
    s=s.lower()
    s=s.replace(" ", "")
    return s == s[::-1]

print(palindrome(query))