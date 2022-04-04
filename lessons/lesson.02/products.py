class Product:

    TYPE = "product"

    def __init__(self, name: str, price: float):
        self._name = name
        # self._price = price
        self.price = price
        self.__inner_value = "foobar"

    @property
    def name(self):  # getter
        return self._name

    @name.setter
    def name(self, value):  # setter
        print("check access to set name.. (TODO)", value)
        self._name = value

    def make_discount(self, discount: int) -> None:
        self.price *= ((100 - discount) / 100)
        # self.price = self.price * ((100 - discount) / 100)
        # return self.price
        # return self.price * ((100 - discount) / 100)

    def some_method(self):
        print("I have access!", self.__inner_value)

    def __str__(self) -> str:
        return self.name
        # return f"{self.__class__.__name__}(name={self.name!r})"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r})"
        # return f"<{self.__class__.__name__}>(name={self.name!r})"


class Phone(Product):
    TYPE = "phone"


class NoteBook(Product):
    TYPE = "laptop"

    def __init__(self, name: str, price: float, backlit_keyboard: bool):
        super().__init__(name, price)
        # self.name = "name"
        self.backlit_keyboard = backlit_keyboard


# def vars(obj):
#     return obj.__dict__


def main():
    product1 = Phone("Galaxy S", 1000)
    print(type(product1))
    print(isinstance(product1, Product))
    print(isinstance(product1, NoteBook))
    print(isinstance(product1, Phone))
    print(product1)
    print([product1])

    product2 = NoteBook("MacBook", 2000, True)
    print(type(product2))
    print(isinstance(product2, Product))
    print(isinstance(product2, NoteBook))
    print(isinstance(product2, Phone))
    print(product2)
    print(vars(product2))

    product1.name = "iPhone"
    print(product1)

    product1._name = "Honor"
    print(product1)

    print(vars(product1))
    product1.some_method()
    # print(product1.__inner_value)
    product1.__inner_value = "fizzbuzz"
    print(vars(product1))
    print(product1.__inner_value)
    print(product1._Product__inner_value)
    product1.some_method()

    print(vars(product1))
    print(product1.__dict__)

    print(repr(product1.name))
    print([product1.name])

    print(product1)
    print([product1])

    print(f"as str: {product1}")
    print(f"as repr: {product1!r}")
    print(f"as repr: {repr(product1)}")

    print(product1.TYPE)
    print(product2.TYPE)

    product1.make_discount(10)
    product2.make_discount(20)
    print(vars(product1))
    print(vars(product2))


if __name__ == '__main__':
    main()
