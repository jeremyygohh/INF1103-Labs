import json
import os

def load_inventory():
    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        with open("inventory.json", "r") as file:
            inventory = json.load(file)

        print("Inventory loaded successfully.")
        return inventory

    else:
        print("inventory.json not found.")
        print("Starting with empty inventory.")
        return []

inventory = load_inventory()

def save_inventory():
    print("Saving inventory...")

    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

    print("Inventory saved successfully to inventory.json.")

def display_all():
    print("Current Inventory")
    print("------------------------------------------------")

    for product in inventory:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )

    print("------------------------------------------------")

def add_product():
    print("Add New Product")

    product_id = input("Enter Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }

    inventory.append(product)

def update_stock():
    print("Update Stock")

    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            print("Product Found:")
            print("Name:", product["name"])
            print("Current Stock:", product["stock"])

            new_stock = int(input("New Stock Quantity: "))
            product["stock"] = new_stock

            print("Stock updated successfully!")
            return

    print("Product not found.")

def search_product():
    print("Search Product")

    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            print("Product Found")
            print("------------------------------------------------")
            print("ID:", product["id"])
            print("Name:", product["name"])
            print(f"Price: ${product['price']:.2f}")
            print("Stock:", product["stock"])
            print("------------------------------------------------")
            return

    print("Product not found.")


display_all()
# add_product()
# save_inventory()