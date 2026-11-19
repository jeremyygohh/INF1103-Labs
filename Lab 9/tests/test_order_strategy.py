
import unittest

from order import Order
from supplier import Supplier
from digital_product import DigitalProduct

from discount_strategy import (
    BulkDiscount,
    PercentageDiscount,
    StudentDiscount
)


class TestOrderStrategy(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier(
            "S001", "Test Supplier", "test@example.com"
        )

        self.product = DigitalProduct(
            "D001", "Software", 250.0,
            10, 500.0, self.supplier
        )

    def test_default_no_discount(self):
        order = Order("ORD001")
        order.add_order_line(self.product, 1)

        self.assertEqual(
            order.calculate_total(), 250.0
        )

    def test_bulk_discount(self):
        order = Order(
            "ORD002", BulkDiscount(200, 20)
        )

        order.add_order_line(self.product, 1)

        self.assertEqual(
            order.calculate_total(), 230.0
        )

    def test_change_discount(self):
        order = Order(
            "ORD003", BulkDiscount(200, 20)
        )

        order.add_order_line(self.product, 1)

        order.set_discount(
            PercentageDiscount(10)
        )

        self.assertEqual(
            order.calculate_total(), 225.0
        )

        order.set_discount(StudentDiscount(5))

        self.assertEqual(
            order.calculate_total(), 237.5
        )


if __name__ == "__main__":
    unittest.main()
