Number_of_items = int(input("Number of items: "))

total_cost = 0

for i in range(1, Number_of_items+1):
    Price_of_item = float(input("Price of item: "))
    total_cost = total_cost + Price_of_item
if total_cost > 100:
    total_cost = total_cost * 0.9

print(f"Total price for {Number_of_items} items is ${total_cost:.2f}")