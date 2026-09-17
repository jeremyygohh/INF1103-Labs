inventory = 0
failed_entries = 0
deliveries_processed = 0

def get_valid_input():
    failed = 0
    while True:
        stock = input("Enter stock quantity: ")

        if stock == "quit":
            return stock, failed

        elif stock.startswith("-"):
            print("Negative numbers are not allowed")
            failed += 1
            continue

        elif not stock.isdigit():
            print("Invalid input")
            failed += 1
            continue

        stock = int(stock)
        return stock, failed
    
def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

def generate_report(total_deliveries, failed_attempts):
    print("Total Deliveries Processed:", total_deliveries)
    print("Number of Failed/Rejected Entries:", failed_attempts)


while True:
    stock, failed = get_valid_input()
    failed_entries += failed

    if stock == "quit":
        break

    inventory = process_delivery(inventory, stock)
    tax = calculate_tax(stock)
    deliveries_processed += 1

generate_report(deliveries_processed, failed_entries)