import unittest
from main import Category, Product

class TestCategory(unittest.TestCase):
    def test_category_initialization(self):
        category = Category("Электроника", "Категория для электронных устройств")
        self.assertEqual(category._name, "Электроника")
        self.assertEqual(category._description, "Категория для электронных устройств")
        self.assertEqual(len(category._products), 0)

    def test_category_add_product(self):
        category = Category("Электроника", "Категория для электронных устройств")
        product = Product("Ноутбук", 1500.0, 10)
        category.add_product(product)
        self.assertIn(product, category._products)
        self.assertEqual(len(category._products), 1)

    def test_category_str(self):
        category = Category("Электроника", "Категория для электронных устройств")
        self.assertEqual(str(category), "Электроника, количество продуктов: 0 шт.")

class TestProduct(unittest.TestCase):
    def test_product_initialization(self):
        product = Product("Ноутбук", 1500.0, 10)
        self.assertEqual(product._name, "Ноутбук")
        self.assertEqual(product._price, 1500.0)
        self.assertEqual(product._quantity, 10)

    def test_product_str(self):
        product = Product("Ноутбук", 1500.0, 10)
        self.assertEqual(str(product), "Ноутбук, 1500.0 руб. Остаток: 10 шт.")

    # Измененный вариант теста test_product_add

    def test_product_add(self):
        laptop = Product("Laptop", 1500.0, 10)
        smartphone = Product("Smartphone", 1000.0, 5)
        result_product = laptop + smartphone
        self.assertEqual(result_product.price, (1500.0 * 10 + 1000.0 * 5) / (10 + 5))
        self.assertEqual(result_product.quantity, 15)


if __name__ == '__main__':
    unittest.main()
