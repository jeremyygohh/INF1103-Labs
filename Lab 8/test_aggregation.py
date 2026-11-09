
from inventory import Inventory
from supplier import Supplier
from physical_product import PhysicalProduct

# Create a Supplier
supplier = Supplier(
    "S001", "Tech Supplier", "tech@example.com"
)

# Create a Product independently
product = PhysicalProduct(
    "P001", "Laptop", 1200.0, 10, 2.5, supplier
)

# Create two inventories
inventory_a = Inventory()
inventory_b = Inventory()

# Test 1: Add Product to Inventory A
inventory_a.add_product(product)

print("Product in Inventory A:")
print(inventory_a.find_product("P001") is product)

# Test 2: Remove Product from Inventory A
removed = inventory_a.remove_product("P001")

print("\nProduct removed successfully:")
print(removed)

print("Product still in Inventory A:")
print(inventory_a.find_product("P001"))

# Test 3: Check whether Product still exists
print("\nProduct after removal:")
product.display_information()

# Test 4: Transfer Product to Inventory B
inventory_b.add_product(product)

print("\nSame Product object in Inventory B:")
print(inventory_b.find_product("P001") is product)
