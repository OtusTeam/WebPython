class Point:
    class_attribute = "spam and eggs"

    def __init__(self, x, y, next_point=None):
        # self.class_attribute = "spam and eggs"

        self.x = x
        self.y = y
        self.next_point = next_point

    def __str__(self):
        return f"Point(x={self.x}, y={self.y}, next={self.next_point})"


def main():
    print(Point)
    print(Point.class_attribute)
    # point = Point()
    # point.x = 1
    # point.y = 2
    point1 = Point(23, 45)
    print(point1)
    print(point1.class_attribute)
    point2 = Point(67, 89, point1)
    print(point2)
    print(point2.class_attribute)

    print(vars(point1))
    print(vars(point2))

    point1.class_attribute = "foo"
    point2.class_attribute = "bar"

    print(Point.class_attribute)
    print(point1.class_attribute)
    print(point2.class_attribute)

    point1.x = 123
    point2.y = 456

    print(point1)
    print(point1.x)
    print(vars(point1))
    print(point2)
    print(point2.y)
    print(vars(point2))

    print(point1)
    print(point2)
    point2.next_point.y = 765
    print(point1)
    print(point2)

    print(point2.next_point is point1)


if __name__ == '__main__':
    main()


