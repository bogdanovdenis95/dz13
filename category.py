class Category:
    def __init__(self, name, description, products=None):
        self._name = name
        self._description = description
        self._products = products if products is not None else []

    def add_product(self, product):
        self._products.append(product)

    @property
    def products_info(self):
        info = ""
        for product in self._products:
            info += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return info