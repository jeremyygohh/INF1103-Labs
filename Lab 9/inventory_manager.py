import json
import os

from product import Product
from inventory import Inventory
from product_factory import ProductFactory
from supplier import Supplier


def load_inventory():
    inventory = Inventory()
    suppliers = {}

    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        with open("inventory.json", "r") as file:
            data = json.load(file)

        for item in data:
            supplier_data = item.get("supplier") or {
                "supplier_id": "UNASSIGNED",
                "name": "Unassigned",
                "contact_email": ""
            }

            supplier_id = supplier_data["supplier_id"]

            if supplier_id not in suppliers:
                suppliers[supplier_id] = Supplier(
                    supplier_id,
                    supplier_data["name"],
                    supplier_data["contact_email"]
                )

            supplier = suppliers[supplier_id]

            product_type = item.get("type")

            if product_type is None:
                raise ValueError(
                    f"Product {item['id']} is missing its type."
                )

            product = ProductFactory.create(
                product_type=product_type,
                product_id=item["id"],
                name=item["name"],
                price=item["price"],
                stock=item["stock"],
                supplier=supplier,
                weight=item.get("weight", 0.0),
                download_size=item.get("download_size", 0.0)
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

    print("Select Product Type:")
    print("1. Physical Product")
    print("2. Digital Product")

    product_type = input("Enter choice (1 or 2): ")
    if product_type not in ("1", "2"):
        print("Invalid product type! Please select 1 or 2.")
        return

    name = input("Product Name: ")
    price = get_positive_float("Enter price: ")
    stock = int(input("Stock Quantity: "))

    print("Enter Supplier Information")
    supplier_id = input("Supplier ID: ")
    supplier_name = input("Supplier Name: ")
    supplier_email = input("Supplier Email: ")

    supplier = Supplier(
        supplier_id,
        supplier_name,
        supplier_email
    )


    extra = {}

    if product_type == "1":
        selected_type = "physical"
        extra["weight"] = float(
            input("Enter weight (kg): ")
        )

    else:
        selected_type = "digital"
        extra["download_size"] = float(
            input("Enter download size (MB): ")
        )

    product = ProductFactory.create(
        product_type=selected_type,
        product_id=product_id,
        name=name,
        price=price,
        stock=stock,
        supplier=supplier,
        **extra
    )

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
        product.get_supplier().display_information()
        print("------------------------------------------------")
    else:
        print("Product not found.")


def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                print("Please enter a number greater than zero.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number, e.g. 12.50")


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