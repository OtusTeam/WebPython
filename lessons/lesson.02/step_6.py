class User:
    MIN_AGE = 18

    def __init__(self):
        self.name = None
        self._age = None
        self._address = None

    @property
    def address(self):  # lazy attrib
        if self._address is None:
            self._address = 'compl logic'
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def age(self):
        # print(self.MIN_AGE)
        return self._age

    @age.setter
    def age(self, value):
        self._age = int(value)
        if self._age < self.MIN_AGE:
            raise ValueError

    def year_older(self):
        self._age += 1


user_1 = User()
user_2 = User()

user_1.name = 'Ivan'
user_1.age = '18'
user_1.year_older()
print(user_1.age)
print(user_1.address)
print(vars(user_1))
print(vars(User))
