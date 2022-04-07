class ShopItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, price={self.price})"

    def __repr__(self):
        return str(self)


class Smartphone(ShopItem):
    pass


class Tablet(ShopItem):
    pass


class Basket:
    def __init__(self):
        self._items = []

    def add(self, item: ShopItem):
        self._items.append(item)

    def __iadd__(self, other: ShopItem):
        self.add(other)
        return self

    def __getitem__(self, index) -> ShopItem:
        return self._items[index]

    def __setitem__(self, index: int, value: ShopItem):
        if not isinstance(index, int):
            raise TypeError("index must be int")

        if not isinstance(value, ShopItem):
            raise TypeError("value must be ShopItem")

        self._items[index] = value

    def __iter__(self):
        return (si for si in self._items)

    def __contains__(self, item):
        return item in self._items

    def __len__(self):
        return len(self._items)


basket = Basket()
phone = Smartphone("iPhone", 999.99)
# print(phone)
# print([phone])
# print(repr(phone))
# print(f"phone: {phone}")
# print(f"phone: {phone!r}")

tablet = Tablet("Galaxy Tab", 1299.99)
# basket.add(phone)
# basket.add(tablet)

basket += phone
print("tablet in basket?", tablet in basket)

basket += tablet
print("tablet in basket?", tablet in basket)


print(basket._items)
print(basket[0])
print(basket[1])
# print(basket[2])

basket[0] = tablet
basket[1] = phone
# basket["1"] = phone
# basket[3] = 123

print(basket._items)

for item_ in basket:
    print(item_)

print(len(basket))
