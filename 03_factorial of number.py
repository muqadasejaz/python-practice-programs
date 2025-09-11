'''
Write a program which can compute the factorial of a  numbers.
Suppose the following input is supplied to the program:
8
Then, the output should be: 40320
'''

def fac(num):
    if (num == 0 or num ==1 ):
        return 1
    else:
        return (num * fac(num - 1))

num = int(input("Enter a number:"))
res = fac(num)
print("the factorical is:", res)
    

