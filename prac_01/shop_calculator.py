total = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid input")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price = float(input("Price of item: $"))
    total += price
if total > 100:
    total -= total * 0.1
print(f"Total price for {number_of_items} items is ${total:.2f}")
