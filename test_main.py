import unittest
from category import Category
from product import Product

class TestCategory(unittest.TestCase):
    def test_category_initialization(self):
        electronics_category = Category("Электроника", "Категория для электронных устройств")
        self.assertEqual(electronics_category._name, "Электроника")
        self.assertEqual(electronics_category._description, "Категория для электронных устройств")
        self.assertEqual(len(electronics_category._products), 0)

    def test_category_add_product(self):
        electronics_category = Category("Электроника", "Категория для электронных устройств")
        laptop = Product("Ноутбук", 1500.0, 10)
        electronics_category.add_product(laptop)
        self.assertIn(laptop, electronics_category._products)
        self.assertEqual(len(electronics_category._products), 1)

class TestProduct(unittest.TestCase):
    def test_product_initialization(self):
        laptop = Product("Ноутбук", 1500.0, 10)
        self.assertEqual(laptop._name, "Ноутбук")
        self.assertEqual(laptop._price, 1500.0)
        self.assertEqual(laptop._quantity, 10)

    def test_product_str_method(self):
        laptop = Product("Ноутбук", 1500.0, 10)
        self.assertEqual(str(laptop), "Ноутбук, 1500.0 руб. Остаток: 10 шт.")

    def test_product_add_method(self):
        laptop = Product("Ноутбук", 1500.0, 10)
        smartphone = Product("Смартфон", 1000.0, 20)
        result_product = laptop + smartphone
        self.assertEqual(result_product, 35000.0)

if __name__ == '__main__':
    unittest.main()
