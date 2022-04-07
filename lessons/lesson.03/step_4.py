class MyStr(str):

    def __add__(self, other) -> "MyStr":
        return self.__class__(f"{self}{other}")

    def __radd__(self, other):
        return self.__class__(f"{other}{self}")


a = MyStr("abc")

# a - 1

print(1 + a)

