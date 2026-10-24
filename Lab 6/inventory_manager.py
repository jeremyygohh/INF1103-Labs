import json
import os

from product import Product
from inventory import Inventory

def load_inventory():
    inventory = Inventory()

    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        with open("inventory.json", "r") as file:
            data = json.load(file)

        for item in data:
            product = Product(
                item["id"],
                item["name"],
                item["price"],
                item["stock"]
            )

            inventory.add_product(product)

        print("Inventory loaded successfully.")

    else:
        print("inventory.json not found.")
        print("Starting with empty inventory.")

    return inventory

def save_inventory(exit_mode=False):
    if not exit_mode:
        print("Saving inventory...")

    products_data = []

    for product in inventory.get_products():
        products_data.append(product.to_dict())

    with open("inventory.json", "w") as file:
        json.dump(products_data, file, indent=4)

    if exit_mode:
        print("Inventory saved successfully.")
    else:
        print("Inventory saved successfully to inventory.json.")

def add_product():
    print("Add New Product")

    product_id = input("Enter Product ID: ")
    if inventory.search_product(product_id) is not None:
        print("Product ID already exists!")
        return
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    product = Product(product_id, name, price, stock)

    inventory.add_product(product)

    print("Product added successfully!")

def update_stock():
    print("Update Stock")

    product_id = input("Enter Product ID: ")

    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product Found:")
    product.display_information()

    new_stock = int(input("New Stock Quantity: "))

    if new_stock < 0:
        print("Stock cannot be negative.")
        return

    product.update_stock(new_stock)

    print("Stock updated successfully!")

def search_product():
    print("Search Product")

    product_id = input("Enter Product ID: ")

    product = inventory.search_product(product_id)

    if product is not None:
        print("Product Found")
        print("------------------------------------------------")
        product.display_information()
        print("------------------------------------------------")
    else:
        print("Product not found.")


def display_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================")

inventory = load_inventory()

while True:
    display_menu()

    option = input("Enter option: ")

    if option == "1":
        inventory.display_all()

    elif option == "2":
        add_product()

    elif option == "3":
        update_stock()

    elif option == "4":
        search_product()

    elif option == "5":
        save_inventory()

    elif option == "6":
        print("Saving inventory before exit...")
        save_inventory(True)
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break

    else:
        print("Invalid option. Please enter 1 to 6.")