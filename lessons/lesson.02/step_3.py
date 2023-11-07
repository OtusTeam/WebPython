class User:
    def __init__(self):
        self.name = None
        self._age = None
        self._address = None

    def get_address(self):
        return self._address or 'undefined'

    def set_address(self, address):
        self._address = address

    def get_age(self):
        return self._age

    def set_age(self, value):
        self._age = int(value)

    def year_older(self):
        self._age += 1




user_1 = User()
user_2 = User()

user_1.name = 'Ivan'
# user_1._age = 25
# user_1.set_age(25)
user_1.set_age('25')
user_1.year_older()
print(user_1.get_age())
print(user_1.get_address())
print(vars(user_1))
