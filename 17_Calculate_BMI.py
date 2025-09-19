#write a program to calculate the body mass index (BMI) from a user's weight and height.


def main():
    while True:
        try:
          weight=float(input("Enter your weight in kg: "))
          height=float(input("Enter your height in meters: "))
          bmi=weight/(height**2)
          print("Your BMI is: ", round(bmi,2))
          break
        except:
            print("Invalid input. Please enter numeric values for weight and height.")
    

main()
