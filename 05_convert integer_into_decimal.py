#write a program to convert integer into decimal

import decimal
number=int(input("enter the integer number:"))

result=decimal.Decimal(number)
print(f"the decimal value of {number} is {result:.1f}")


