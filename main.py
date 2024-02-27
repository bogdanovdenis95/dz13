from category import Category
from product import Product, Smartphone, LawnGrass

if __name__ == "__main__":
    electronics_category = Category("Электроника", "Категория для электронных устройств")
    laptop = Product("Ноутбук", 1500.0, 10)
    smartphone = Smartphone("Смартфон", 1000.0, 20, "высокая", "Samsung Galaxy", "64 ГБ", "черный")
    lawn_grass = LawnGrass("Трава газонная", 50.0, 100, "Россия", "2 недели", "зеленый")

    electronics_category.add_product(laptop)
    electronics_category.add_product(smartphone)
    electronics_category.add_product(lawn_grass)

    print(electronics_category)

