from product import Product

class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

if __name__ == "__main__":
    laptop = PhysicalProduct("P001", "Laptop", 1000, 5, 2)
    laptop.display_information()
    print(laptop.get_fulfilment_info())