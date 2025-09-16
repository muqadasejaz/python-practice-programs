# Write a program to find the sum of the numbers from 1 to n using while loop

n=int(input("enter the number: "))

i=1
sum=0
if n > 0:
    while i<=n:
        sum+=i
        i+=1
        print("the sum ", sum)