class Solver:
    ERR_TEXT = "can't multiply strings"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
        # return 13

    def mul(self):
        if (
            not isinstance(self.a, (int, float))
            or not isinstance(self.b, (int, float))
        ):
            raise TypeError(self.ERR_TEXT)

        return self.a * self.b


def div(a, b):
    return a / b

# import testing
# import testing.test_solver
# from testing import test_solver
#
# print(testing)
# print(testing.SPAM)
