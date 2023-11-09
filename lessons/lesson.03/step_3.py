MIN_AGE = 18


def _parse_int(value):
    try:
        return int(value)
    except ValueError:
        raise WrongIntValue


def _age_validator(value):
    _age = _parse_int(value)
    if _age < MIN_AGE:
        raise WrongAgeValue
    return _age


class WrongIntValue(Exception):
    pass


class WrongAgeValue(Exception):
    pass


class User:
    MIN_AGE = 18

    def __init__(self, name, age, address=None):
        self.name = name
        self._age = _age_validator(age)
        self._address = address

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
        return self._age

    @staticmethod
    def _parse_int(value):
        try:
            return int(value)
        except ValueError:
            raise WrongIntValue

    # def _age_validator(self, value):
    #     _age = self._parse_int(value)
    #     if _age < self.MIN_AGE:
    #         raise WrongAgeValue
    #     return _age

    def year_older(self):
        self._age += 1


class AdminUser(User):
    MIN_AGE = 25
    MAX_AGE = 75

    def __init__(self, name, age, address, level=0):
        super().__init__(name, age, address)
        self.level = level

    # def _age_validator(self, value):
    #     super()._age_validator(value)
    #
    #     if self._age > self.MAX_AGE:
    #         raise ValueError


user_1 = AdminUser('Ivan', '26', 'Moscow')

user_1.year_older()
print(vars(user_1))
