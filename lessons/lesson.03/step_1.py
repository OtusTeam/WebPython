from __future__ import annotations

# age: int = 1
# age = 1
#
# age = "23"
age = "42"
# age: int = 42
#
# # age = []
# # age = {}
# # age = ()
#
# age + 1
# age + 1
# age + 1
#
# print(age)


class MyStr(str):

    # def __add__(self, other) -> "MyStr":
    def __add__(self, other) -> MyStr:
        # return MyStr(f"{self}{other}")
        return self.__class__(f"{self}{other}")

    # def __mul__(self, other):
    # def __dir__(self) -> Iterable[str]:

    def __sub__(self, other: int) -> MyStr:
        # print("other: ", other)
        return self.__class__(self[:-other])


name = MyStr("OTUS")
# name = str("OTUS")
print(name)
print(name + " Hello")
print(name + 123)

a = MyStr("abc")
b = 123
# c = "def"
c = 456
# c + b
print(a + b)
print(a + b + c)

print(["a", "b"] + ["c", "d"])

print(a + b + c - 4)


print(a - b)
print(a[0])
print(a[1])
print(a[2])
print(a[1:3])
print(a[0:2])
print(a[:2])
print(a[:])
print(a[:         -1])
print(a[:(len(a) - 1)])

print(a - 1)
