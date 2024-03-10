from abc import ABC, abstractmethod

class AbstractProduct(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def calculate_total_price(self):
        pass

    @classmethod
    @abstractmethod
    def create_product(cls, name, description, price, quantity):
        pass


class Product(AbstractProduct):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, цена: {self.price}"

    def calculate_total_price(self):
        return self.price * self.quantity

    @classmethod
    def create_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)


class LoggingMixin:
    def __repr__(self):
        return f"Создан объект: {self.__class__.__name__}"


class Smartphone(Product, LoggingMixin):
    def __init__(self, name, description, price, quantity, performance, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color


    def __str__(self):
        return f"{self.name}, цена: {self.price}, описание: {self.description}"

    def calculate_total_price(self):
        return self.price * self.quantity

# В классе LawnGrass
class LawnGrass(Product, LoggingMixin):
    def __init__(self, name, description, price, quantity, country_of_origin, germination_period, color):
        super().__init__(name, description, price, quantity)  # Добавлен аргумент description
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color


    def __str__(self):
        return f"{self.name}, цена: {self.price}, описание: {self.description}"

    def calculate_total_price(self):
        return self.price * self.quantity

