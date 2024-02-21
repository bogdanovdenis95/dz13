import unittest
from category import Category
from product import Product

class TestCategory(unittest.TestCase):
    def test_category_initialization(self):
        category = Category("Электроника", "Категория для электронных устройств")
        self.assertEqual(category._name, "Электроника")
        self.assertEqual(category._description, "Категория для электронных устройств")
        self.assertEqual(category._products, [])

    def test_category_add_product(self):
        category = Category("Электроника", "Категория для электронных устройств")
        product = Product("Ноутбук", 1500.0, 10)
        category.add_product(product)
        self.assertIn(product, category._products)

class TestProduct(unittest.TestCase):
    def test_product_initialization(self):
        product = Product("Ноутбук", 1500.0, 10)
        self.assertEqual(product._name, "Ноутбук")
        self.assertEqual(product._price, 1500.0)
        self.assertEqual(product._quantity, 10)

    def test_create_product_class_method(self):
        product_data = {
            "name": "Планшет",
            "price": 1000.0,
            "quantity": 5,
        }
        product = Product.create_product(**product_data)
        self.assertEqual(product._name, "Планшет")
        self.assertEqual(product._price, 1000.0)
        self.assertEqual(product._quantity, 5)

if __name__ == '__main__':
    unittest.main()