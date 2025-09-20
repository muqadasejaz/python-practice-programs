#write the program to reverse a name entered by the user.


while True:
    try:
        name = input("Enter your name: ")
        if not name.isalpha():
            raise ValueError("Name should only contain alphabetic characters.")
        
        reversed_name = name[::-1]
        print(f"Reversed name: {reversed_name}")
        break
    except:
        print("An unexpected error occurred. Please try again.")