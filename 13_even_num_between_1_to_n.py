# Write a program to print only even numbers between 1 to n using while loop

n=int(input("enter the number: "))

i=2
if n>0:
    while i <=n:
        print(i, end=" ") 
        i+=2
else:
    print("No even numbers in the given range.")