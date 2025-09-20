#write a program to calculate the area of a triangle given its base and height.


while True:
    try:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))    
        
        area = 0.5 * base * height
        print(f"The area of the triangle is {area}.")
        break
    except:
        print("Invalid input. Please enter numeric values.")