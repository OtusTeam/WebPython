class MyStr(str):

    def __add__(self, other) -> "MyStr":
        return self.__class__(f"{self}{other}")

    def __iadd__(self, other):
        return self.__add__(other)


a = MyStr("abc")

a += 123

print(a)
