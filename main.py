
from category import Category
from product import Product

if __name__ == "__main__":
    electronics_category = Category("Electronics", "Category for electronic devices")
    laptop = Product("Laptop", 1500.0, 10)
    smartphone = Product("Smartphone", 1000.0, 20)

    electronics_category.add_product(laptop)
    electronics_category.add_product(smartphone)

    print(electronics_category.products_info)


