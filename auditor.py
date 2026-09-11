inventory = 0
failed_entries = 0

while True:
    stock = input("Enter stock quantity: ")

    if stock == "quit":
        break

    elif stock.startswith("-"):
        print("Negative numbers are not allowed")
        failed_entries += 1
        continue

    elif not stock.isdigit():
        print("Invalid input")
        failed_entries += 1
        continue

    stock = int(stock)
    inventory += stock

    if inventory > 500:
        print("Inventory Exceeded")
        break

print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", failed_entries)