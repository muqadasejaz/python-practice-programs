# Python Practice Programs for Logic Building 💻

This repository contains simple Python practice programs designed to improve **logic building** and **problem-solving skills**.  
The goal is to start from very basic concepts and gradually move towards more challenging problems.  

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📂 Programs

1. **Hello World with Name**  
   - A beginner program that prints `"Hello world, <your name>"`.  
   - **Purpose:** Understand Python syntax and the `print()` function.  

2. **Number is Even or Odd**  
   - A program that checks whether a given number is even or odd.  
   - **Purpose:** Practice conditional statements (`if-else`) and modulus operator (`%`).

3. **Factorial of a Number**  
   - A program that computes the factorial of a given number.    
   - **Purpose:** Practice loops/recursion and mathematical logic.  
   - **Example Input:** `5`  
   - **Example Output:** `120`

4. **Swap Two Numbers**  
   - A program that swaps the values of two numbers using a temporary variable.  
   - **Purpose:** Practice variables and value swapping.

5. **Convert Integer into Decimal**  
   - A program that converts an integer input into a decimal value using the `decimal` module.  
   - **Purpose:** Practice type conversion and formatting output.
  
6. **Table of a number**  
   - A program that prints the multiplication table of a number entered by the user.  
   - **Purpose:** Practice `for` loops and basic arithmetic.

7. **Area of a Circle**  
   - A program that calculates the area of a circle using the formula **π × r²**.  
   - **Purpose:** Practice mathematical formulas and formatted output.

8. **Perimeter of a Rectangle**  
   - A program that calculates the perimeter of a rectangle using the formula **2 × (length + width)**.  
   - **Purpose:** Practice mathematical formulas and user input handling.

9. **Check Positive, Negative or Zero**  
   - A program that checks whether a given number is positive, negative, or zero.  
   - **Purpose:** Practice conditional statements (`if-elif-else`).

10. **Maximum Between Three Numbers**  
    - A program that finds the maximum among three numbers using conditional statements.  
    - **Purpose:** Practice nested conditions and comparison operators.
   
11. **Middle Number Among Three Numbers**  
    - A program that finds the middle number in a group of three numbers.  
    - **Purpose:** Practice logical operators (`and`, `or`) and conditional statements.
   
12. **Sum of Numbers from 1 to n**  
    - A program that calculates the sum of all numbers from 1 to `n` using a `while` loop.  
    - **Purpose:** Practice loops, counters, and accumulation logic.
   
13. **Print Even Numbers Between 1 to n using While Loop**

  📖 Description
  This program takes an integer `n` as input and prints all the even numbers between `1` and `n` using a `while` loop.  
  If the given number is less than 2, the program informs that no even numbers exist in the range.

14. **Check if a String is Palindrome or Not**

 📖 Description:
This program checks whether a given string is a **palindrome** or not.  
A palindrome is a word, phrase, number, or sequence of characters that reads the same **forward and backward**, ignoring case and spaces.  

Examples of palindromes:  
- `madam`  
- `racecar`  
- `Never odd or even`  

 📝 Logic
-  Convert the input string to lowercase.  
-  Remove spaces to handle multi-word strings.  
-  Reverse the string using slicing (`s[::-1]`).  
-  Compare the original string with its reversed version.  
-  If they match → It's a palindrome, otherwise not.  


15. **Check Voting Eligibility**

 📖 Description:
This program checks whether a person is **eligible to vote** based on their age.  
According to general rules, a person must be **18 years or older** to vote.

 📝 Logic
- Take the user's age as input.  
- If age is greater than or equal to 18 → Eligible to vote.  
- Otherwise → Not eligible to vote.  


16. **Check Whether a Character is a Vowel or Not**

 📖 Description:
This program checks whether a given character is a **vowel** or not.  
Vowels are: `a, e, i, o, u` (both uppercase and lowercase).

📝 Logic
- Take a character as input.  
- Check if it belongs to the set of vowels (`a, e, i, o, u, A, E, I, O, U`).  
- If yes → Print that it is a vowel.  
- Otherwise → Print that it is not a vowel.

17. **Calculate Body Mass Index (BMI)**

📖 Description:
This program calculates the **Body Mass Index (BMI)** based on the user's **weight** (in kilograms) and **height** (in meters).  
The BMI is a measure that helps classify whether a person is underweight, normal weight, overweight, or obese.

📝 Logic
- Take weight (kg) and height (m) as input from the user.  
- Use the formula `BMI = weight / (height ** 2)`.  
- Round the result to 2 decimal places.  
- Handle invalid (non-numeric) input using `try-except`.

18. **Check if a Number is Divisible by Another Number**

📖 Description:
This program checks whether a given number (**dividend**) is divisible by another number (**divisor**).  
It ensures that the divisor properly divides the dividend without leaving a remainder.

📝 Logic
- Take two numbers as input:  
   - First number → Dividend  
   - Second number → Divisor  
- Use the modulus operator (`%`) to check divisibility.
- If `num1 % num2 == 0` → The number is divisible.  
- Otherwise → It is not divisible.  
- Handle invalid inputs with `try-except`.

19. **Calculate the Area of a Triangle**

📝 Logic
- Take the base and height of the triangle as input.  
- Apply the formula `area = 0.5 * base * height`.  
- Display the result.  
- Handle invalid (non-numeric) inputs with `try-except`.

20. **Reverse a Name Entered by the User**

📖 Description:
This program takes a **name** as input and prints it in **reverse order**.  
It also validates that the input contains only alphabetic characters.

📝 Logic
- Take the user's name as input.  
- Validate that the input contains only alphabets (`isalpha()`).  
- Reverse the string using slicing (`[::-1]`).  
- Print the reversed name.  
- Handle invalid inputs using `try-except`.  

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🚀 Getting Started

1. Clone the repository:  
 ```bash
   git clone https://github.com/muqadasejaz/python-practice-programs.git
 ```

2. Run a program:
```bash
python 01_hello_world.py
python 02_even_or_odd.py
python 03_factorial of number.py
python 04_swap two numbers.py
python 05_convert_integer_into_decimal.py
python 06_table_of_a_number.py
python 07_area_of_circle.py
python 08_perimeter_of_rectangle.py
python 09_nature_of_a_number.py
python 10_maximum_number.py
python 11_find_middle_number_among_three_numbers.py
python 12_sum_of_numbers_from_1_to_n.py
python 13_even_num_between_1_to_n.py
python 14_string_palindrome_or_not.py
python 15_check_voting_eligibility.py
python 16_vowel_or_not.py
python 17_Calculate_BMI.py
python 18_divisibility.py
python 19_area_of_triangle.py
python 20_reverse_name.py
```

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🎯 Goals

- Strengthen logical thinking through coding  
- Practice Python basics step by step  
- Build a foundation for solving larger coding problems  
- Encourage consistency in problem-solving practice  

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📌 Upcoming Additions

- More beginner-friendly programs (loops, functions, lists)  
- Intermediate logic-based problems (patterns, recursion, searching/sorting)  
- File handling and exception handling examples  
- Small projects combining multiple concepts

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 👤 Author

Muqadas Ejaz

BS Computer Science (AI Specialization)

AI/ML Engineer

Data Science & Gen AI Enthusiast

📫 Connect with me on [LinkedIn](https://www.linkedin.com/in/muqadasejaz/)  

🌐 GitHub: [github.com/muqadasejaz](https://github.com/muqadasejaz)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📎 License

This project is open-source and available under the [MIT License](LICENSE).
