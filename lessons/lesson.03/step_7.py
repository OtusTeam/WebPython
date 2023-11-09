class Vector:
    def __init__(self, *values):
        self._values = values
        self._values_set = set(values)

    def __add__(self, other) -> 'Vector':
        return self.__class__(
            *(
                a + b
                for a, b in zip(self._values, other._values)
            ),
        )

    def __iadd__(self, other):
        self._values = [
            a + b
            for a, b in zip(self._values, other._values)
        ]
        return self

    def __str__(self):
        return str(self._values)

    def __repr__(self):
        return f'{self.__class__.__name__}{self._values}'

    def __iter__(self):
        print('__iter__')
        return (el for el in self._values)

    def __contains__(self, item):
        print('__contains__')
        return item in self._values_set

    def __len__(self):
        return len(self._values)

    def __getitem__(self, item):
        return self._values[item]

    # def __getattribute__(self, item):
    #     pass

    # def __getattr__(self, item):
    #     pass


a = Vector(25, 30)
print(id(a))
a += a
print(id(a))
print(25 in a)  # O(n) -> O(1)
print(50 in a)  # O(n) -> O(1)
# iterable VS Iterator
# iterable -> Iterator -> __iter__
# Iterator -> next() -> __next__
# __iter__ + __next__ = iterable + Iterator
for el in a:
    print(el)

print(len(a))
print(a[0])
# a[0] = 22

# a.idx_0
# a.idx_1
# a.idx_2
