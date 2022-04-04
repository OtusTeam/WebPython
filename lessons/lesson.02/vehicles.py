class BaseVehicle:
    def __init__(self, weight):
        self.weight = weight

    def make_sound(self):
        return None


class Car(BaseVehicle):
    def __init__(self, weight, wheels):
        print("car's super init", super(Car, self).__init__)
        super().__init__(weight)
        self.wheels = wheels

    def make_sound(self):
        # old = super().make_sound()
        # print("old was:", old)
        return "beep"

    def lets_ride(self):
        print("vroom")


class Ship(BaseVehicle):
    def __init__(self, weight, color):
        super().__init__(weight)
        self.color = color

    def make_sound(self):
        return "boop"

    def set_sail(self):
        print("set sail!")


class Amphibian(Car, Ship):
    def __init__(self, weight, wheels, color):
        # Car.__init__(self, weight, wheels)
        # Ship.__init__(self, weight, color)
        # (super(Ship, self).__init__)

        self.weight = weight
        self.wheels = wheels
        self.color = color


if __name__ == '__main__':
    amphibian = Amphibian(1234, 6, "green")
    print(Amphibian.mro())
    print(Amphibian.__mro__)

    print(vars(amphibian))

    amphibian.set_sail()
    amphibian.lets_ride()

    print(amphibian.make_sound())
