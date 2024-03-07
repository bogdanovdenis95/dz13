import unittest
from product import Category, Product, Smartphone, LawnGrass


class TestSmartphone(unittest.TestCase):
    def test_smartphone_creation(self):
        smartphone = Smartphone("Смартфон", "Мощный смартфон", 800.0, 5, "Высокая", "Модель X", "16 ГБ", "Черный")
        self.assertEqual(smartphone.name, "Смартфон")
        self.assertEqual(smartphone.description, "Мощный смартфон")
        self.assertEqual(smartphone.price, 800.0)
        self.assertEqual(smartphone.quantity, 5)
        self.assertEqual(smartphone.performance, "Высокая")
        self.assertEqual(smartphone.model, "Модель X")
        self.assertEqual(smartphone.memory, "16 ГБ")
        self.assertEqual(smartphone.color, "Черный")

    def test_smartphone_str(self):
        smartphone = Smartphone("Смартфон", "Мощный смартфон", 800.0, 5, "Высокая", "Модель X", "16 ГБ", "Черный")
        expected_string = "Смартфон, цена: 800.0, описание: Мощный смартфон"
        self.assertEqual(str(smartphone), expected_string)

    def test_smartphone_calculate_total_price(self):
        smartphone = Smartphone("Смартфон", "Мощный смартфон", 800.0, 5, "Высокая", "Модель X", "16 ГБ", "Черный")
        expected_total_price = 800.0 * 5
        self.assertEqual(smartphone.calculate_total_price(), expected_total_price)

class TestLawnGrass(unittest.TestCase):
    def test_lawn_grass_creation(self):
        lawn_grass = LawnGrass("Трава газонная", "Качественная трава для газона", 20.0, 100, "USA", "14 дней", "Зеленая")
        self.assertEqual(lawn_grass.name, "Трава газонная")
        self.assertEqual(lawn_grass.description, "Качественная трава для газона")
        self.assertEqual(lawn_grass.price, 20.0)
        self.assertEqual(lawn_grass.quantity, 100)
        self.assertEqual(lawn_grass.country_of_origin, "USA")
        self.assertEqual(lawn_grass.germination_period, "14 дней")
        self.assertEqual(lawn_grass.color, "Зеленая")

    def test_lawn_grass_str(self):
        lawn_grass = LawnGrass("Трава газонная", "Качественная трава для газона", 20.0, 100, "USA", "14 дней", "Зеленая")
        expected_string = "Трава газонная, цена: 20.0, описание: Качественная трава для газона"
        self.assertEqual(str(lawn_grass), expected_string)

    def test_lawn_grass_calculate_total_price(self):
        lawn_grass = LawnGrass("Трава газонная", "Качественная трава для газона", 20.0, 100, "USA", "14 дней", "Зеленая")
        expected_total_price = 20.0 * 100
        self.assertEqual(lawn_grass.calculate_total_price(), expected_total_price)

class TestCategory(unittest.TestCase):
    def test_category_initialization(self):
        electronics_category = Category("Электроника", "Категория для электронных устройств")
        self.assertEqual(electronics_category.name, "Электроника")
        self.assertEqual(electronics_category.description, "Категория для электронных устройств")
        self.assertEqual(electronics_category.products, [])

    def test_add_product(self):
        electronics_category = Category("Электроника", "Категория для электронных устройств")
        smartphone = Smartphone("Смартфон", "Мощный смартфон", 800.0, 5, "Высокая", "Модель X", "16 ГБ", "Черный")
        electronics_category.add_product(smartphone)
        self.assertEqual(len(electronics_category.products), 1)
        self.assertEqual(electronics_category.products[0], smartphone)

if __name__ == "__main__":
    unittest.main()
