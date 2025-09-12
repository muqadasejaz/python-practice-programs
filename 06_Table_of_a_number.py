#write a program to print the table of a number entered by user


number=int(input("enter the number to print its table: "))

for i in range(1,11):
    result=number*i
    print(f"{number} X {i}= {result}")