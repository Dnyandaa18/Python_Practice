# Implementing a simple calculator in Python using basic arithmetic operations, userinput, and conditional statements.

operator = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = round(num1 / num2, 2)
else:
    print("Invalid operator")
    exit()

print(f"The result is: {result}")