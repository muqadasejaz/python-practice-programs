#write a program to check whether a given number is divisible by another number.

while True:
    try:
        num1 = int(input("Enter the first number (dividend): "))
        num2 = int(input("Enter the second number (divisor): "))    
        
        if num1%num2 == 0:
           print(f"{num1} is divisible by {num2}.")
        else:
            print(f"{num1} is not divisible by {num2}.")
        break
    except:
        print("Invalid input. Please enter integer values.")