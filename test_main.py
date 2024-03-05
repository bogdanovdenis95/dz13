import unittest
from product import Smartphone, LawnGrass
from category import Category

class TestProduct(unittest.TestCase):
    def test_product_creation(self):
        laptop = Smartphone("Ноутбук", "Описание ноутбука", 1500.0, 10, "высокая", "Acer", "128 ГБ", "серебристый")
        self.assertEqual(laptop.name, "Ноутбук")
        self.assertEqual(laptop.price, 1500.0)
        self.assertEqual(laptop.quantity, 10)

    def test_product_str(self):
        laptop = Smartphone("Ноутбук", "Описание ноутбука", 1500.0, 10, "высокая", "Acer", "128 ГБ", "серебристый")
        self.assertEqual(str(laptop), "Ноутбук, цена: 1500.0, описание: Описание ноутбука")

    def test_product_add(self):
        laptop1 = Smartphone("Ноутбук", "Описание ноутбука", 1500.0, 10, "высокая", "Acer", "128 ГБ", "серебристый")
        laptop2 = Smartphone("Ноутбук", "Описание ноутбука", 1500.0, 5, "высокая", "Acer", "128 ГБ", "серебристый")
        result_price = laptop1.calculate_total_price() + laptop2.calculate_total_price()
        self.assertEqual(result_price, 22500.0)  # Проверяем правильность вычисления суммы цен

class TestCategory(unittest.TestCase):
    def test_category_initialization(self):
        electronics_category = Category("Электроника", "Категория для электронных устройств")
        self.assertEqual(electronics_category.name, "Электроника")
        self.assertEqual(electronics_category.description, "Категория для электронных устройств")
        self.assertEqual(len(electronics_category.products), 0)

    def test_category_add_product(self):
        electronics_category = Category("Электроника", "Категория для электронных устройств")
        laptop = Smartphone("Ноутбук", "Описание ноутбука", 1500.0, 10, "высокая", "Acer", "128 ГБ", "серебристый")
        electronics_category.add_product(laptop)
        self.assertIn(laptop, electronics_category.products)

if __name__ == '__main__':
    unittest.main()
