
import unittest
import tempfile

from pathlib import Path
from io import StringIO
from contextlib import redirect_stdout

from csv_loader import load_products
from inventory import Inventory
from supplier import Supplier


class TestCSVLoader(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.csv_path = Path(self.temp_dir.name) / "products.csv"

        self.inventory = Inventory()

        self.supplier = Supplier(
            "S001", "Test Supplier", "test@example.com"
        )

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_valid_and_invalid_rows(self):
        self.csv_path.write_text(
            "product_type,product_id,name,price,stock_quantity\n"
            "physical,P001,Desk Lamp,25.00,10\n"
            "digital,D001,Photo Editor,49.90,100\n"
            "service,S001,Installation,30.00,5\n"
            "physical,P002,Office Chair,abc,3\n"
            "physical,P003,Monitor Stand,39.50,7\n"
        )

        output = StringIO()

        with redirect_stdout(output):
            load_products(
                str(self.csv_path),
                self.inventory,
                self.supplier
            )

        self.assertEqual(
            len(self.inventory.get_products()), 3
        )

        self.assertIn("Row 4 skipped:", output.getvalue())
        self.assertIn("Row 5 skipped:", output.getvalue())
        self.assertIn("3 products loaded.", output.getvalue())
        self.assertIn(
            "Load attempt finished.", output.getvalue()
        )

    def test_missing_file(self):
        missing_path = Path(self.temp_dir.name) / "missing.csv"
        output = StringIO()

        with redirect_stdout(output):
            load_products(
                str(missing_path),
                self.inventory,
                self.supplier
            )

        self.assertIn(
            "Products file not found:", output.getvalue()
        )

        self.assertIn(
            "Load attempt finished.", output.getvalue()
        )

        self.assertEqual(
            len(self.inventory.get_products()), 0
        )

    def test_all_valid_products(self):
        self.csv_path.write_text(
            "product_type,product_id,name,price,stock_quantity\n"
            "physical,P001,Mouse,20.00,10\n"
            "digital,D001,Software,50.00,5\n"
        )

        output = StringIO()

        with redirect_stdout(output):
            load_products(
                str(self.csv_path),
                self.inventory,
                self.supplier
            )

        self.assertEqual(
            len(self.inventory.get_products()), 2
        )

        self.assertIn("2 products loaded.", output.getvalue())
        self.assertNotIn("skipped", output.getvalue())

    def test_negative_price_skipped(self):
        self.csv_path.write_text(
            "product_type,product_id,name,price,stock_quantity\n"
            "physical,P001,Invalid Mouse,-20.00,10\n"
            "physical,P002,Valid Mouse,20.00,10\n"
        )

        output = StringIO()

        with redirect_stdout(output):
            load_products(
                str(self.csv_path),
                self.inventory,
                self.supplier
            )

        self.assertEqual(
            len(self.inventory.get_products()), 1
        )

        self.assertIn("Row 2 skipped:", output.getvalue())
        self.assertIn("1 products loaded.", output.getvalue())


if __name__ == "__main__":
    unittest.main()
