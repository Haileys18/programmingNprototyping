#Hailey Sooknanan
#1/7/2025
#CFU18-Writes a program that adds up all of the prices 
# Version 1
prices = [1.95, 4.5, 0.99, 5.99]
total = 0

for price in prices:
    total += price

print(f"Total: ${total:.2f}")
# Version 2 & 3
items = []  # List for item names
prices = []  # List for item prices

num_items = int(input("How many items do you want to add? "))

for _ in range(num_items):
    item_name = input("Enter the name of the item: ")
    item_price = float(input("Enter the price of the item: "))
    items.append(item_name)
    prices.append(item_price)

# Print the receipt
print("\nReceipt:")
print("Item Name       Price")
print("---------------------")


for i in range(len(items)):
    print(f"{items[i]:<15}${prices[i]:.2f}")

total = sum(prices)
print("---------------------")
print(f"Total:          ${total:.2f}")


