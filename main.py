from category import Category
from product import Smartphone, LawnGrass

if __name__ == "__main__":
    electronics_category = Category("Электроника", "Категория для электронных устройств")
    smartphone = Smartphone("Смартфон", "Описание смартфона", 1000.0, 20, "высокая", "Samsung Galaxy", "64 ГБ", "черный")
    lawn_grass = LawnGrass("Трава газонная", "Описание травы", 50.0, 100, "Россия", "2 недели", "зеленый")

    electronics_category.add_product(smartphone)
    electronics_category.add_product(lawn_grass)

    print(electronics_category)

