# Create a shopping cart program that will continuously ask the user for a food product and its price.
# Have an exit clause if the user wishes to stop adding more things to the cart.
# At the end, show the food items and the total cost to the user.

foods = []
prices = []

while True:
    food = input("Enter a food product (or press Q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of the {food} product: R "))
        foods.append(food)
        prices.append(price)

# Display the final cart and grand total after exiting the loop
print("\n---------- YOUR FINAL CART ----------")
for food in foods:
    print(food, end=" ")

# Calculate the grand total
total = 0
for price in prices:
    total += price

print("\n-------------------------------")
print(f"Grand Total: R {total}")