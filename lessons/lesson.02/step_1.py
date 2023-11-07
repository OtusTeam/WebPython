def set_address(self, address):
    print(user_1)


class User:
    # def __new__(cls, *args, **kwargs) -> self:
    #     pass

    def __init__(self):
        self.name = None
        self.age = None
        self.address = None

    def set_address(self, address):
        pass


# descriptors
user_1 = User()
user_2 = User()

print(vars(user_1))
print(user_1.__dict__)
