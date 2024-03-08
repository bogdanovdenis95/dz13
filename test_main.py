import unittest
from category import Category
from product import Product, Smartphone, LawnGrass

class TestCategory(unittest.TestCase):
    def test_category_initialization(self):
        electronics_category = Category("Электроника", "Категория для электронных устройств")
        self.assertEqual(electronics_category.name, "Электроника")
        self.assertEqual(electronics_category.description, "Категория для электронных устройств")
        self.assertEqual(len(electronics_category.products), 0)

    def test_category_add_product(self):
        electronics_category = Category("Электроника", "Категория для электронных устройств")
        smartphone = Smartphone("Смартфон", "Мощный смартфон", 800.0, 5, "Высокая", "Модель X", "16 ГБ", "Черный")
        lawn_grass = LawnGrass("Трава газонная", "Качественная трава для газона", 20.0, 100, "USA", "14 дней", "Зеленая")

        electronics_category.add_product(smartphone)
        electronics_category.add_product(lawn_grass)

        self.assertEqual(len(electronics_category.products), 2)
        self.assertIn(smartphone, electronics_category.products)
        self.assertIn(lawn_grass, electronics_category.products)

class TestProduct(unittest.TestCase):
    def test_product_creation(self):
        smartphone = Smartphone("Смартфон", "Мощный смартфон", 800.0, 5, "Высокая", "Модель X", "16 ГБ", "Черный")
        self.assertEqual(smartphone.name, "Смартфон")
        self.assertEqual(smartphone.description, "Мощный смартфон")
        self.assertEqual(smartphone.price, 800.0)
        self.assertEqual(smartphone.quantity, 5)

    def test_product_str(self):
        smartphone = Smartphone("Смартфон", "Мощный смартфон", 800.0, 5, "Высокая", "Модель X", "16 ГБ", "Черный")
        self.assertEqual(str(smartphone), "Смартфон, цена: 800.0, описание: Мощный смартфон")

class TestLoggingMixin(unittest.TestCase):
    def test_logging_mixin(self):
        electronics_category = Category("Электроника", "Категория для электронных устройств")
        self.assertEqual(str(electronics_category), "Электроника, количество продуктов: 0 шт.")

        smartphone = Smartphone("Смартфон", "Мощный смартфон", 800.0, 5, "Высокая", "Модель X", "16 ГБ", "Черный")
        lawn_grass = LawnGrass("Трава газонная", "Качественная трава для газона", 20.0, 100, "USA", "14 дней", "Зеленая")

        electronics_category.add_product(smartphone)
        electronics_category.add_product(lawn_grass)

        self.assertEqual(str(electronics_category), "Электроника, количество продуктов: 2 шт.")

if __name__ == "__main__":
    unittest.main()
