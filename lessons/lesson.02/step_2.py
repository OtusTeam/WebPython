class User:
    def __init__(self):
        self.name = None
        self.__age = None  # name mangling, private
        self._address = None  # protected

    def set_address(self, address):
        pass

    def _set_age(self, value):
        pass

    def get_address(self):
        return self._address


user_1 = User()
user_2 = User()

print(vars(user_1))
# print(user_1.__dict__)
print(user_1.name)
print(user_1._address)
user_1._address = 'Moscow'

print(vars(user_1))

# MongoMixin()


class MongoUser(MongoMixin, User):  # C3
    pass


