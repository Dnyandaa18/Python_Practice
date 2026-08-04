# Compound interest calculator

principal = 0
rate = 0
time = 0
n = 0

while principal <= 0:
    principal = float(input("Enter the principal amount (greater than 0): "))
    if principal <= 0:
        print("Principal amount must be greater than 0. Please try again.")
        
while rate <= 0:
    rate = float(input("Enter the annual interest rate (greater than 0): "))
    if rate <= 0:
        print("Interest rate must be greater than 0. Please try again.")

while time <= 0:
    time = float(input("Enter the time period (greater than 0): "))
    if time <= 0:
        print("Time period must be greater than 0. Please try again.")

while n <= 0:
    n = int(input("Enter the number of times interest is compounded per year (greater than 0): "))
    if n <= 0:
        print("Number of compounding periods must be greater than 0. Please try again.")
total_amount = principal * (1 + (rate / 100) / n) ** (n * time)
print(f"The total amount after {time} years is: {total_amount:.2f}")