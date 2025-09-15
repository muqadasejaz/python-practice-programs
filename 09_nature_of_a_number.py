# Write a program to check whether a given number is positive,negative or zero

num=int(input("enter the num: "))

if num > 0:
    print(num, " is positive number")
elif num < 0:
    print(num, " is negative number")
else:
    print(num, ": num is a zero")