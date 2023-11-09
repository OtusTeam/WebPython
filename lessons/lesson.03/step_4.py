class WrongIntValue(Exception):
    pass


class WrongAgeValue(Exception):
    pass


class User:
    # qty = 0
    MIN_AGE = 18

    def __init__(self, name, age, address=None):
        self.name = name
        self._age = self._age_validator(age)
        self._address = address
        self._superuser = False

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

    @classmethod
    def _age_validator(cls, value):
        # self.name
        # self._age
        # self._address
        _age = cls._parse_int(value)
        if _age < cls.MIN_AGE:
            raise WrongAgeValue
        return _age

    @classmethod
    def create_superuser(cls, *args, **kwargs):
        # cls.qty += 1
        inst = cls(*args, **kwargs)
        inst._superuser = True
        return inst

    # @staticmethod
    # def create_superuser(*args, **kwargs):
    #     inst = User(*args, **kwargs)
    #     inst._superuser = True
    #     return inst

    def year_older(self):
        self._age += 1


class AdminUser(User):
    MIN_AGE = 25
    MAX_AGE = 75

    def __init__(self, name, age, address, level=0):
        super().__init__(name, age, address)
        self.level = level

    @classmethod
    def _age_validator(cls, value):
        _age = super()._age_validator(value)

        if _age > cls.MAX_AGE:
            raise ValueError

        return _age

    # @staticmethod
    # def create_superuser(*args, **kwargs):
    #     inst = AdminUser(*args, **kwargs)
    #     inst._superuser = True
    #     return inst


# user_1 = AdminUser('Ivan', '26', 'Moscow')
user_1 = AdminUser.create_superuser('Ivan', '26', 'Moscow')

# user_1._superuser = True
user_1.year_older()
print(vars(user_1))
print(type(user_1))
