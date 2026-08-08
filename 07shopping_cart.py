foods = []
prices = []
total = 0

while True:
    food = input("Enter a food you want to buy(q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}:$"))
        foods.append(food)
        prices.append(price)

print("----- Your Cart-----")
for fruit in foods:
    print(fruit)
for pric in prices:
    total += price

print(f"Your total of all the items is :{total}")