from pytest import raises, fixture, mark, param
from solver import solve_square_equation, INVALID_TYPE_ERROR_TEXT


@fixture(scope="module")
def square_equation_data():
    return 1, -70, 600


class TestSquareEquationSolver:
    def test_raises_type_error(self):
        with raises(TypeError) as exc_info:
            solve_square_equation(0, "1", 1)
        assert str(exc_info.value) == INVALID_TYPE_ERROR_TEXT

    def test_return_type_tuple(self, square_equation_data):
        res = solve_square_equation(*square_equation_data)
        assert isinstance(res, tuple)

    def test_solves(self, square_equation_data):
        x1, x2 = solve_square_equation(*square_equation_data)
        assert x1 == 60
        assert x2 == 10

    @mark.parametrize("args, expected_res", [
        param(
            (3, -14, -5), (5, -1/3),
            id="result ok",
        ),
        param(
            (1, -6, 9), (3, None),
            id="only one root",
        ),
        param(
            (1, 1, 9), (None, None),
            id="no roots",
        ),
    ])
    def test_solves_different_values(self, args, expected_res):
        res = solve_square_equation(*args)
        assert res == expected_res
