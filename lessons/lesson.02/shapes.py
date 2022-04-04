class Shape:
    def get_area(self):
        print("no data for area")


class Rectangle(Shape):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        # self.area = a * b

    def get_area(self):
        return self.a * self.b


class Square(Rectangle):
    # noinspection PyMissingConstructor
    def __init__(self, a):
        # super().__init__(a, a)
        self.a = a

    @property
    def b(self):
        return self.a


def main():
    rectangle = Rectangle(3, 4)
    print(rectangle.get_area())
    # print(rectangle.area)
    rectangle.a = 5
    print(rectangle.get_area())
    # print(rectangle.area)

    square = Square(6)
    print(square.get_area())
    print(square.a)
    print(square.b)

    square.a = 5

    print(square.a)
    print(square.b)
    print(square.get_area())


if __name__ == '__main__':
    main()
