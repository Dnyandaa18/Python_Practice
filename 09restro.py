# Implementing Dict

menu = {"Coffee": 3.00,
        "Nachos": 2.50,
        "Pizza": 7.60,
        "Burger": 6.70,
        "Roll": 4.98,
        "Faluda": 5.00 }
cart = []
total = 0

print("---------MENU-----------")

for key,value in menu.items():
    print(f"{key:9}: ${value:.2f}")

print("------------------------")

while True:
    food = input("Select an item(q to quit): ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("-------YOUR ORDER--------")

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()  
print(f"Total is: ${total:.2f}")