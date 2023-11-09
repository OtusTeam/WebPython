# import step_0
#
# print(step_0.User.MIN_AGE)
class User:
    MIN_AGE = 18

    def __init__(self, name, age, address=None):
        self.name = name
        self._age = None
        self._address = address

        self._age_setter(age)

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

    def _age_setter(self, value):
        self._age = int(value)
        if self._age < self.MIN_AGE:
            raise ValueError

    def year_older(self):
        self._age += 1


class AdminUser(User):
    MIN_AGE = 25
    MAX_AGE = 75

    def __init__(self, name, age, address, level=0):
        super().__init__(name, age, address)
        self.level = level

    # def _age_setter(self, value):
    #     self._age = int(value)
    #     if (
    #             self._age <= self.MIN_AGE
    #             or self._age > self.MAX_AGE
    #     ):
    #         raise ValueError
    def _age_setter(self, value):
        super()._age_setter(value)

        if self._age > self.MAX_AGE:
            raise ValueError


user_1 = AdminUser('Ivan', '26', 'Moscow')

user_1.year_older()
print(vars(user_1))
print(isinstance(user_1, AdminUser))
