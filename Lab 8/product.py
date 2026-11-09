
from abc import ABC, abstractmethod
from supplier import Supplier


class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__supplier: Supplier = supplier

    def update_stock(self, quantity):
        if quantity >= 0:
            self.__stock = quantity

    def display_information(self):
        print(f"Product ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")

    def get_product_id(self):
        return self.__product_id

    def get_supplier(self) -> Supplier:
        return self.__supplier

    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "supplier": self.__supplier.to_dict()
        }

    def get_price(self) -> float:
        return self.__price

    @abstractmethod
    def get_fulfilment_info(self):
        pass
