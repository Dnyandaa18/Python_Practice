weight = float(input("Enter the weight: "))
unit = input("Kilograms (kg) or Pounds (lb): ").lower()
if unit == "kg":
    converted_weight = weight * 2.20462
    print(f"{weight} kg is equal to {converted_weight:.2f} lb")
elif unit == "lb":
    converted_weight = weight / 2.20462
    print(f"{weight} lb is equal to {converted_weight:.2f} kg")
else: 
    print("Invalid unit")