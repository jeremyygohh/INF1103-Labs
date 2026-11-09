
from product import Product
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


supplier = Supplier(
    "S001", "Tech Supplier", "tech@example.com"
)

laptop = PhysicalProduct(
    "P001", "Laptop", 1200.0, 10, 2.5, supplier
)

software = DigitalProduct(
    "D001", "Software", 50.0, 100, 500.0, supplier
)

print("Physical Product:")
show_product_details(laptop)

print("\nDigital Product:")
show_product_details(software)

# Create an inventory
inventory = Inventory()

# Add both product types
inventory.add_product(laptop)
inventory.add_product(software)

print("\n--- Inventory LSP Test ---")

# Display both products
inventory.display_all()

# Update stock using the same inherited method
laptop.update_stock(5)
software.update_stock(20)

print("\n--- After Stock Update ---")
inventory.display_all()
