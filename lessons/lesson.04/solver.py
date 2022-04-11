class Solver:

    EXC_TYPE_ERROR_TEXT = "can't multiply two strings"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        res = self.a + self.b
        print("res:", res)
        return res

    def mul(self):
        # self.a * self.b
        if (
            isinstance(self.a, str) and
                isinstance(self.b, str)):
            raise TypeError(self.EXC_TYPE_ERROR_TEXT)
        # if self.a == 3:
        #     return 0
        return self.a * self.b
