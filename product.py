from abc import ABC, abstractmethod

class LoggingMixin:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        attributes = ', '.join([f"{key}={value}" for key, value in self.__dict__.items()])
        return f"{self.__class__.__name__}({attributes})"



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




class Product(AbstractProduct, LoggingMixin):
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, цена: {self.price}"

    def calculate_total_price(self):
        return self.price * self.quantity

    @classmethod
    def create_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)


class Smartphone(Product, LoggingMixin):
    def __init__(self, name, description, price, quantity, performance, model, memory, color):
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, цена: {self.price}, описание: {self.description}"

    def calculate_total_price(self):
        return self.price * self.quantity

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', description='{self.description}', price={self.price}, quantity={self.quantity}, performance='{self.performance}', model='{self.model}', memory='{self.memory}', color='{self.color}')"

    @classmethod
    def create_product(cls, name, description, price, quantity, performance, model, memory, color):
        return cls(name, description, price, quantity, performance, model, memory, color)


class LawnGrass(Product, LoggingMixin):
    def __init__(self, name, description, price, quantity, country_of_origin, germination_period, color):
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)


    def __str__(self):
        return f"{self.name}, цена: {self.price}, описание: {self.description}"

    def calculate_total_price(self):
        return self.price * self.quantity

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', description='{self.description}', price={self.price}, quantity={self.quantity}, country_of_origin='{self.country_of_origin}', germination_period='{self.germination_period}', color='{self.color}')"

    @classmethod
    def create_product(cls, name, description, price, quantity, country_of_origin, germination_period, color):
        return cls(name, description, price, quantity, country_of_origin, germination_period, color)