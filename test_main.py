import unittest
from category import Category
from product import Product, Smartphone


class TestProduct(unittest.TestCase):
    def test_product_creation(self):
        laptop = Product("Ноутбук", 1500.0, 10)
        self.assertEqual(laptop.name, "Ноутбук")
        self.assertEqual(laptop.price, 1500.0)
        self.assertEqual(laptop.quantity, 10)

    def test_product_str(self):
        laptop = Product("Ноутбук", 1500.0, 10)
        self.assertEqual(str(laptop), "Ноутбук, цена руб. 1500.0. Остаток: 10 шт.")

    def test_product_add(self):
        laptop1 = Product("Ноутбук", 1500.0, 10)
        smartphone = Smartphone("Смартфон", 1000.0, 5, "высокая", "модель", "64ГБ", "черный")
        with self.assertRaises(TypeError):
            result_product = laptop1 + smartphone


class TestCategory(unittest.TestCase):
    def test_category_initialization(self):
        electronics_category = Category("Электроника", "Категория для электронных устройств")
        self.assertEqual(electronics_category.name, "Электроника")
        self.assertEqual(electronics_category.description, "Категория для электронных устройств")
        self.assertEqual(len(electronics_category.products), 0)

    def test_category_add_product(self):
        electronics_category = Category("Электроника", "Категория для электронных устройств")
        laptop = Product("Ноутбук", 1500.0, 10)
        electronics_category.add_product(laptop)
        self.assertIn(laptop, electronics_category.products)

if __name__ == '__main__':
    unittest.main()
