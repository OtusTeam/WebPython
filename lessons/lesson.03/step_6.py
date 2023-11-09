class Vector:
    def __init__(self, *values):
        self._values = values

    def __add__(self, other) -> 'Vector':
        # return [
        #     a + b for a, b in zip(self._values, other._values)
        # ]
        # result = []
        # for idx in range(len(self._values)):
        #     result.append(self._values[idx] + other._values[idx])
        # return self.__class__(*result)

        return self.__class__(
            *(
                a + b
                for a, b in zip(self._values, other._values)
            ),
        )

    def __str__(self):
        return str(self._values)

    # __repr__ = __str__
    def __repr__(self):
        # Vector(25, 30)
        return f'{self.__class__.__name__}{self._values}'


a = Vector(25, 30)
b = Vector(0, 10)
c = a + b + a + a
# print(vars(c))
print(c)
print(str(c))
print(repr(c))

# repr(c)
# c.repr()

data = [a, b, c]
print(data)
c_clone = eval(repr(c))
print(c_clone, type(c_clone))
