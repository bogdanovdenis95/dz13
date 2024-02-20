import unittest
from category import Category
from product import Product

class TestCategory(unittest.TestCase):
    def test_category_initialization(self):
        category = Category("Electronics", "Category for electronic devices")
        self.assertEqual(category._name, "Electronics")
        self.assertEqual(category._description, "Category for electronic devices")
        self.assertEqual(category._products, [])

    def test_category_add_product(self):
        category = Category("Electronics", "Category for electronic devices")
        product = Product("Laptop", 1500.0, 10)
        category.add_product(product)
        self.assertIn(product, category._products)

class TestProduct(unittest.TestCase):
    def test_product_initialization(self):
        product = Product("Laptop", 1500.0, 10)
        self.assertEqual(product._name, "Laptop")
        self.assertEqual(product._price, 1500.0)
        self.assertEqual(product._quantity, 10)

if __name__ == '__main__':
    unittest.main()

