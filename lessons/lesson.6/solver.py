from math import sqrt

INVALID_TYPE_ERROR_TEXT = "all values have to be int or float"


def solve_square_equation(a, b, c):
    if not all(map(
        lambda v: isinstance(v, (int, float)),
        (a, b, c),
    )):
        raise TypeError(INVALID_TYPE_ERROR_TEXT)

    if a == 0:
        if b == 0:
            return None, None
        return -c / b, None

    d = b ** 2 - 4 * a *c
    if d < 0:
        return None, None

    d_root = sqrt(d)
    divider = 2 * a
    x1 = (-b + d_root) / divider
    x2 = (-b - d_root) / divider

    if d == 0:
        x2 = None
    elif x2 > x1:
        x1, x2 = x2, x1

    return x1, x2
