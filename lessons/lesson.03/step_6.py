class User:
    SPAM = "eggs"

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age

    def __str__(self):
        # return self.username
        return f"{self.username} {self.age}"

    def __repr__(self):
        # return str(self)
        return f"{self.__class__.__name__}(username={self.username!r}, age={self.age})"

    def __getattribute__(self, item):
        print("__getattribute__", item)
        return super().__getattribute__(item)

    def __getattr__(self, item):
        print("__getattr__", item)
        # return super().__getattr__(item)
        return f"hello {item}"


john = User("john", 42)
# john = User(username='john', age=42)

print(john)
print([john])
print(john.username)
print(getattr(john, "age"))
print(john.hello)
print(john.help)
print(john.SPAM)
