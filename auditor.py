inventory = 0

while True:
    stock = input("Enter stock quantity: ")

    if stock == "quit":
        break

    elif stock.startswith("-"):
        print("Negative numbers are not allowed")
        continue

    elif not stock.isdigit():
        print("Invalid input")
        continue

    stock = int(stock)
    inventory += stock