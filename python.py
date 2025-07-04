

foods = []
prices = []
total=0
while True:
    food = input("Enter a food to buy or press q to quit: ")
    if food.lower() == 'q':
        break
    try:
        price = float(input(f"Enter the price of the {food}: R"))
        foods.append(food)
        prices.append(price)
    except ValueError:
        print("Please enter a valid number.")
        continue

    print("---- YOUR CART ----")
    for f in foods:
        print(f, end=" ")
    print("\n")

# Calculate total once after the loop ends
total = sum(prices)
print("---- FINAL TOTAL ----")
print(f"Your total is: R{total:.2f}")

