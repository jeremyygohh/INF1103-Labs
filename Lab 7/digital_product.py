from product import Product

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size} MB")

    def get_fulfilment_info(self):
            return "This product is delivered digitally."

if __name__ == "__main__":
    game = DigitalProduct("D001", "Minecraft", 50, 10, 500)
    game.display_information()
    print(game.get_fulfilment_info())