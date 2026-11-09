from product import Product

class Inventory:
    def __init__(self) -> None:
        self.__products: list[Product] = []

    
    def remove_product(self, product_id: str) -> bool:
        for product in self.__products:
            if product.get_product_id() == product_id:
                self.__products.remove(product)
                return True

        return False


    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    
    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product

        return None


    def search_product(self, product_id: str) -> Product | None:
        return self.find_product(product_id)

    def display_all(self) -> None:
        print("Current Inventory")
        print("------------------------------------------------")

        if not self.__products:
            print("No products available.")
            return

        for product in self.__products:
            product.display_information()
            print("------------------------------------------------")

    def get_products(self) -> list[Product]:
        return self.__products.copy()