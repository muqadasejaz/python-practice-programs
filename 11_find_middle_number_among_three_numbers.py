# Write a program to find the middle number in a group of three numbers

"""
Description:

The logic in this question is that if we have 3 numbers like a,b and c so in this case if we say a is a
middle number then there is a two conditions. first is that a is greater than b and less than c.
the second condition is that a is less than b and greater than c. and in this case both conditions works
at the same time with the logical operator 'or'.
"""

num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
num3=int(input("enter the third number: "))

if ((num1 > num2) and (num1 < num3)) or ((num1 < num2) and (num1 > num3)):
    print(num1 , " is the middle number")
elif ((num2 > num1) and (num2 < num3)) or ((num2 < num1) and (num2 > num3)):
     print(num2 , " is the middle number")
else:
     print(num3 , " is the middle number")