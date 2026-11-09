
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order import Order

# Create supplier
supplier = Supplier(
    "S001", "Tech Supplier", "tech@example.com"
)

# Create products
laptop = PhysicalProduct(
    "P001", "Laptop", 1200.0, 10, 2.5, supplier
)

software = DigitalProduct(
    "D001", "Software", 50.0, 100, 500.0, supplier
)

# Test 1: Create Order A
order_a = Order("ORD001")

order_a.add_order_line(laptop, 2)
order_a.add_order_line(software, 3)

print("Order A:")
for line in order_a.order_lines:
    print(f"Product: {line.product.get_product_id()}")
    print(f"Quantity: {line.quantity}")
    print(f"Subtotal: ${line.calculate_subtotal():.2f}")

print(f"Order A Total: ${order_a.calculate_total():.2f}")

# Test 2: Create Order B using the same laptop
order_b = Order("ORD002")
order_b.add_order_line(laptop, 1)

print("\nOrder B:")
print(f"Order B Total: ${order_b.calculate_total():.2f}")

# Test 3: Compare objects
print("\nSame OrderLine object:")
print(order_a.order_lines[0] is order_b.order_lines[0])

print("Same Product object:")
print(
    order_a.order_lines[0].product
    is order_b.order_lines[0].product
)

# Test 4: Remove Order A
del order_a

print("\nAfter removing Order A:")
laptop.display_information()

print(f"Order B Total: ${order_b.calculate_total():.2f}")
