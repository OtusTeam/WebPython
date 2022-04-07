
class MyStr(str):
    def __add__(self, other) -> "MyStr":
        return self.__class__(f"{self}{other}")


str = MyStr

# list = [1, 2, 3]

a = str("abc")

print(a + 123)
