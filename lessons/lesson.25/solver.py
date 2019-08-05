from math import sqrt
from typing import Tuple, Optional


def square_equation_solver(a, b, c) -> Tuple[Optional[float], Optional[float]]:
    if not any(map(
            lambda v: isinstance(v, (int, float)),
            (a, b, c),
    )):
        raise TypeError

    if a == 0:
        if b == 0:
            return None, None
        return -c / b, None

    d = b * b - 4 * a * c
    root = sqrt(d)
    divider = (2 * a)
    x1 = (-b - root) / divider
    x2 = (-b + root) / divider

    if d == 0:
        x2 = None
    elif x2 > x1:
        x1, x2 = x2, x1

    return x1, x2
