from category import Category
from product import Product

if __name__ == "__main__":
    electronics_category = Category("Электроника", "Категория для электронных устройств")
    laptop = Product("Ноутбук", 1500.0, 10)
    smartphone = Product("Смартфон", 1000.0, 20)

    electronics_category.add_product(laptop)
    electronics_category.add_product(smartphone)

    print(electronics_category)

