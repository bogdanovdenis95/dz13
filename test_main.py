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

class TestSmartphone(unittest.TestCase):
    def test_create_product(self):
        smartphone = Smartphone("Смартфон", "Мобильный телефон", 1000.0, 1, "High", "Model X", "64GB", "Black")
        self.assertTrue(callable(getattr(smartphone, 'create_product', None)), "Method create_product not implemented")

    def test_repr(self):
        smartphone = Smartphone("Смартфон", "Мобильный телефон", 1000.0, 1, "High", "Model X", "64GB", "Black")
        expected_repr = "Smartphone(name=Смартфон, description=Мобильный телефон, price=1000.0, quantity=1, performance=High, model=Model X, memory=64GB, color=Black)"
        self.assertEqual(repr(smartphone), expected_repr)

class TestLawnGrass(unittest.TestCase):
    def test_create_product(self):
        lawn_grass = LawnGrass("Трава газонная", "Газонное растение", 10.0, 10, "USA", "30 days", "Green")
        self.assertTrue(callable(getattr(lawn_grass, 'create_product', None)), "Method create_product not implemented")

    def test_repr(self):
        lawn_grass = LawnGrass("Трава газонная", "Газонное растение", 10.0, 10, "USA", "30 days", "Green")
        expected_repr = "LawnGrass(name=Трава газонная, description=Газонное растение, price=10.0, quantity=10, country_of_origin=USA, germination_period=30 days, color=Green)"
        self.assertEqual(repr(lawn_grass), expected_repr)

if __name__ == '__main__':
    unittest.main()
