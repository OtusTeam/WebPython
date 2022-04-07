
class MyStr(str):
    def __add__(self, other) -> "MyStr":
        return self.__class__(f"{self}{other}")

    def __call__(self, *args, **kwargs):
        kw = (
            f"{key}={value}"
            for key, value in kwargs.items()
        )
        return self.__class__(" ".join((self, *map(str, args), *kw)))


a = MyStr("abc")
print(a(123, 456, "qwerty", None, spam="eggs"))
