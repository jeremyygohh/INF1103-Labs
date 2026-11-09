
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

# Create one Supplier object
supplier = Supplier(
    "S001",
    "Tech Supplier",
    "tech@example.com"
)

# Create two products using the same supplier
physical = PhysicalProduct(
    "P001", "Laptop", 1200.0, 10, 2.5, supplier
)

digital = DigitalProduct(
    "D001", "Software", 50.0, 100, 500.0, supplier
)

# Test 1: Display supplier information
print("Physical Product Supplier:")
physical.get_supplier().display_information()

print("\nDigital Product Supplier:")
digital.get_supplier().display_information()

# Test 2: Check whether they share the same object
print("\nSame Supplier Object:")
print(physical.get_supplier() is digital.get_supplier())

# Test 3: Delete the original supplier variable
del supplier

print("\nAfter deleting supplier variable:")
physical.get_supplier().display_information()
digital.get_supplier().display_information()
