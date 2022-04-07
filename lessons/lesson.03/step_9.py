from string import ascii_letters

VOWELS = "aeiou"


def contains_vowels(name: str):
    return any((letter in name for letter in VOWELS))


class User:

    REQUIRED_AGE = 21

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age

    def __str__(self):
        # return self.username
        return f"{self.username} {self.age}"

    def __repr__(self):
        # return str(self)
        return f"{self.__class__.__name__}(username={self.username!r}, age={self.age})"

    def __eq__(self, other: "User"):
        if not isinstance(other, User):
            return False
        return self.username == other.username and self.age == other.age

    def copy(self):
        return self.__class__(username=self.username, age=self.age)

    @property
    def age_ok(self) -> bool:
        return self.check_age(self.age)

    @classmethod
    def check_age(cls, age: int):
        print(cls)
        return age >= cls.REQUIRED_AGE

    @staticmethod
    def name_contains_vowels(name: str):
        return any((letter in name for letter in VOWELS))

    # contains_vowels = staticmethod(contains_vowels)
    # name_contains_vowels = staticmethod(contains_vowels)


# User.contains_vowels = staticmethod(contains_vowels)


def main():
    user = User("foobar", 123)
    user2 = user
    print(user)
    print(user == user2)
    print(user is user2)

    user3 = user.copy()

    print(user3)
    print(user3 == user2)
    print(user3 is user2)
    user3.username = "spameggs"
    user2.age = 42
    print(user)
    print(user2)
    print(user3)
    user3.age = 20
    print(user3.age_ok)
    print(user2.age_ok)

    print(user.check_age(23))
    print(user.check_age(21))
    print(user.check_age(20))

    print('User.check_age(42)', User.check_age(42))

    print('User.name_contains_vowels("qwwrty")', User.name_contains_vowels("qwwrty"))
    print('User.name_contains_vowels("qwewrty")', User.name_contains_vowels("qwewrty"))
    print('contains_vowels("abc")', contains_vowels("abc"))
    # print('User.contains_vowels("qwewrty")', User.contains_vowels("oj"))


if __name__ == '__main__':
    main()
