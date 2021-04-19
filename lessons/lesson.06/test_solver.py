from unittest import TestCase

import pytest

from solver import Solver, mul


class TestSolverOld(TestCase):

    def test_add(self):
        result = Solver.add(2, 3)
        self.assertEqual(result, 5)


class TestSolver:
    @pytest.mark.parametrize("args, expected_result", [
        ((5, 7), 12),
        ((6, 3), 9),
        ((111, 22), 133),
        ((1, 2), 3),
        pytest.param(
            (0, 0), 0,
            id="sum zeros",
        ),
        pytest.param(
            (-12, -15), -27,
            id="negatives",
        ),
    ])
    def test_add(self, args, expected_result):
        res = Solver.add(*args)
        assert res == expected_result

    def test_sub(self):
        res = Solver.sub(10, 3)
        assert res == 7


def test_mul():
    res = mul(3, 5)
    assert res == 15
