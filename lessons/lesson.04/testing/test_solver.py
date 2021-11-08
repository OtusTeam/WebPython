from unittest import TestCase

import pytest
from pytest import fixture, mark

from solver import Solver, add


@fixture
def solver_instance():
    # print("init solver instance")
    return Solver(6, 7)


# also see indirect
# https://docs.pytest.org/en/6.2.x/example/parametrize.html#apply-indirect-on-particular-arguments

@fixture(params=[
    # (1, "2"),
    # (None, 1),
    # ("3", "1"),
    pytest.param(
        (1, "2"),
        id="second-is-str",
    ),
    pytest.param(
        (None, 1),
        id="first-is-None",
    ),
    pytest.param(
        ("3", "1"),
        id="both-are-str",
    ),
])
def solver_inst(request):
    a, b = request.param
    return Solver(a, b)


class TestSolverTestCase(TestCase):

    def test_add(self):
        s = Solver(2, 3)
        result = s.add()
        self.assertEqual(5, result)
        # self.assertEqual(result, 5)

    # def test_add_negative

    def test_mul(self):
        s = Solver(2, 3)
        result = s.mul()
        self.assertEqual(6, result)


def test_add():
    res = add(4, 5)
    assert res == 9


class TestSolver:
    def test_add(self, solver_instance):
        result = solver_instance.add()
        assert result == 13
        solver_instance.b = 6
        result = solver_instance.add()
        assert result == 12

    def test_add_raises(self, solver_inst):
        with pytest.raises(TypeError) as exc_info:
            solver_inst.add()

        assert str(exc_info.value) == solver_inst.EXC_TYPE_ERROR_ON_MUL

    def test_mul(self, solver_instance):
        result = solver_instance.mul()
        assert result == 42

    @mark.parametrize("a, b", [
        ("2", "3"),
        (3, None),
        (None, None),
        (None, "None"),
        pytest.param(1, "None"),
    ])
    def test_mul_raises(self, a, b):
        s = Solver(a, b)
        with pytest.raises(TypeError) as exc_info:
            s.mul()

        assert str(exc_info.value) == s.EXC_TYPE_ERROR_ON_MUL
