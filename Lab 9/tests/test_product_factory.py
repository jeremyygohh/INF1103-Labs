
import unittest

from product_factory import ProductFactory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier


class TestProductFactory(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier(
            "S001", "Test Supplier", "test@example.com"
        )

    def test_create_physical_product(self):
        product = ProductFactory.create(
            "physical", "P001", "Laptop",
            1200, 10, self.supplier, weight=2.5
        )

        self.assertIsInstance(product, PhysicalProduct)
        self.assertEqual(product.to_dict()["weight"], 2.5)

    def test_create_digital_product(self):
        product = ProductFactory.create(
            "digital", "D001", "Software",
            50, 100, self.supplier, download_size=500
        )

        self.assertIsInstance(product, DigitalProduct)
        self.assertEqual(
            product.to_dict()["download_size"], 500
        )

    def test_unknown_product_type(self):
        with self.assertRaisesRegex(
            ValueError, "Unknown product type: service"
        ):
            ProductFactory.create(
                "service", "S001", "Installation",
                30, 5, self.supplier
            )


if __name__ == "__main__":
    unittest.main()
