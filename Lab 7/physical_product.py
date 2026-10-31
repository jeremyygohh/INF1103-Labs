from product import Product
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

    def calculate_shipping_cost(self):
        return self.__weight * 5

if __name__ == "__main__":
    laptop = PhysicalProduct("P001", "Laptop", 1000, 5, 2)
    laptop.display_information()
    print(laptop.get_fulfilment_info())
    print(f"Shipping Cost: ${laptop.calculate_shipping_cost():.2f}")
    keyboard = PhysicalProduct("P002", "Keyboard", 80, 10, 0.5)
    keyboard.display_information()
    print(keyboard.get_fulfilment_info())
    print(f"Keyboard Shipping Cost: ${keyboard.calculate_shipping_cost():.2f}")