import pytest

from solver import add, square_equation_solver, INVALID_ARGS_TYPE_TEXT


def test_add():
    assert add(1, 2) == 3


class TestSquareEquationSolver:
    def test_solver_raises_on_invalid_args(self):
        with pytest.raises(TypeError) as exc_info:
            square_equation_solver('', 1, 2)
        assert INVALID_ARGS_TYPE_TEXT == str(exc_info.value)

    # @pytest.mark.parametrize('args, expected_result', [
    #     ((-10, 20, 30), (3, -1)),
    #     ((1, 6, -7), (1, -7)),
    # ],
    # ids=(
    #     'a negative',
    #     'c negative',
    # ))
    @pytest.mark.parametrize(
        'args, expected_result',
        [
            pytest.param(
                (-10, 20, 30), (3, -1),
                id='a negative',
            ),
            pytest.param(
                (1, 6, -7), (1, -7),
                id='c negative',
            ),
            pytest.param(
                (0, 10, 20), (-2, None),
                id='a is zero',
            ),
        ]
    )
    def test_solver_works_ok(self, args, expected_result):
        res = square_equation_solver(*args)
        assert res == expected_result

    def test_result_is_tuple(self, default_args):
        res = square_equation_solver(*default_args)
        assert isinstance(res, tuple)
        assert len(res) == 2

    def test_x1_is_bigger(self, default_args):
        res = square_equation_solver(*default_args)
        x1, x2 = res
        assert x1 > x2

    def test_for_default_values(self, default_args, default_expected_result):
        res = square_equation_solver(*default_args)
        assert res == default_expected_result
