from unittest import TestCase

from pytest import fixture, mark, param, raises

from solver import Solver, div


class SolverTestCase(TestCase):

    def setUp(self) -> None:
        self.solver = Solver(2, 3)
        self.solver2 = Solver(5, 8)

    # def tearDown(self) -> None:
    #     self.solver.dispose()

    def test_add(self):
        result = self.solver.add()
        self.assertEqual(result, 5)
        self.solver.a = 6
        result = self.solver.add()
        self.assertEqual(result, 9)

    def test_add_(self):
        result = self.solver2.add()
        self.assertEqual(result, 13)

    def test_mul(self):
        result = self.solver.mul()
        self.assertEqual(result, 6)


@fixture
def solver_instance() -> Solver:
    return Solver(4, 5)


@fixture
def solver_inst(request) -> Solver:
    # print(request.param)
    a, b = request.param
    return Solver(a, b)


@fixture(params=[
    param([2, 3]),
    param((4, 5)),
    (4, 8),
])
def solver_multi(request):
    a, b = request.param
    return Solver(a, b)


# @fixture(params=['conn1', 'conn2'])
# def db_conn():
#     return ...


class TestSolver:
    def test_add(self, solver_instance: Solver):
        result = solver_instance.add()
        assert result == 9

    def test_mul(self, solver_instance: Solver):
        result = solver_instance.mul()
        assert result == 20

    @mark.parametrize("a, b, expected_result", [
        (2, 3, 5),
        (4, 3, 8),
        param(4, 3, 7),
        param(3, 6, 9, id="add-nums"),
        param("3", "6", "36", id="add-strings"),
    ])
    def test_add_(self, a, b, expected_result):
        solver = Solver(a, b)
        result = solver.add()
        assert result == expected_result

    @mark.parametrize("solver_inst, expected_result", [
        param((2, 3), 5, id="nums"),
        param((3, 3), 5, id="nums-2"),
        param(("abc", "qwe"), "abcqwe", id="strs"),
    ], indirect=["solver_inst"])
    def test_add_indirect(self, solver_inst, expected_result):
        assert solver_inst.add() == expected_result

    def test_mul_(self, solver_multi):
        expected_result = solver_multi.a * solver_multi.b
        assert solver_multi.mul() == expected_result

    @mark.parametrize("solver_inst", [
        param(("a", "b")),
        param(("a", 2)),
        param((2, "b")),
        param(([2], "b")),
        param(([2], [])),
    ], indirect=True)
    def test_mul_raises(self, solver_inst):
        with raises(TypeError) as exc_info:
            solver_inst.mul()
        assert str(exc_info.value) == solver_inst.ERR_TEXT


def test_div():
    assert div(10, 2) == 5


def test_div_raises_zero_division():
    with raises(ZeroDivisionError):
        assert div(1, 0)
        # assert div(1, 1)
