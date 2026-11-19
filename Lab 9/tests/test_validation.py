
import unittest

from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order_line import OrderLine


class TestValidation(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier(
            "S001", "Test Supplier", "test@example.com"
        )

        self.product = PhysicalProduct(
            "P001", "Laptop", 1200.0,
            10, 2.5, self.supplier
        )

    def test_zero_price(self):
        with self.assertRaises(ValueError):
            PhysicalProduct(
                "P002", "Mouse", 0,
                10, 0.2, self.supplier
            )

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            DigitalProduct(
                "D001", "Software", -50,
                10, 500, self.supplier
            )

    def test_negative_stock(self):
        with self.assertRaises(ValueError):
            PhysicalProduct(
                "P003", "Keyboard", 50,
                -5, 0.8, self.supplier
            )

    def test_negative_stock_update(self):
        with self.assertRaises(ValueError):
            self.product.update_stock(-3)

    def test_zero_order_quantity(self):
        with self.assertRaises(ValueError):
            OrderLine(self.product, 0)

    def test_negative_order_quantity(self):
        with self.assertRaises(ValueError):
            OrderLine(self.product, -2)

    def test_zero_stock_allowed(self):
        product = DigitalProduct(
            "D002", "Editor", 50,
            0, 500, self.supplier
        )

        self.assertEqual(product.to_dict()["stock"], 0)


if __name__ == "__main__":
    unittest.main()
