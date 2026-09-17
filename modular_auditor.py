inventory = 0
failed_entries = 0

def get_valid_input():
    while True:
        stock = input("Enter stock quantity: ")

        if stock == "quit":
            return stock

        elif stock.startswith("-"):
            print("Negative numbers are not allowed")
            continue

        elif not stock.isdigit():
            print("Invalid input")
            continue

        stock = int(stock)
        return stock

def process_delivery(current_total, new_value):
    new_total = current_total + new_value