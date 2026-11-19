
import unittest

from discount_strategy import (
    NoDiscount,
    PercentageDiscount,
    BulkDiscount,
    StudentDiscount
)


class TestDiscountStrategy(unittest.TestCase):

    def test_no_discount(self):
        strategy = NoDiscount()
        self.assertEqual(strategy.apply(100), 100)

    def test_percentage_discount(self):
        strategy = PercentageDiscount(10)
        self.assertEqual(strategy.apply(200), 180)

    def test_bulk_discount(self):
        strategy = BulkDiscount(200, 20)
        self.assertEqual(strategy.apply(250), 230)

    def test_student_discount(self):
        strategy = StudentDiscount(5)
        self.assertEqual(strategy.apply(100), 95)


if __name__ == "__main__":
    unittest.main()
