from unittest import TestCase

from pytest import fixture, mark, param, raises

from solver import Solver


class SolverTestCase(TestCase):

    def setUp(self) -> None:
        self.s = Solver(2, 3)

    # def setUpClass(cls) -> None:

    def test_add(self):
        # s = Solver(2, 3)
        res = self.s.add()
        self.assertEqual(5, res)

        self.s.a = 5
        res = self.s.add()
        self.assertEqual(8, res)
        # s = Solver(3, 4)
        # res = s.add()
        # self.assertEqual(7, res)

    def test_mul(self):
        # s = Solver(2, 3)
        res = self.s.mul()
        self.assertEqual(6, res)

    # def test_mul__raises(self):
    #     with self.assertRaises(TypeError) as exc_info:
    #         self.s.mul()


# @fixture(scope="function")
@fixture
def solver_instance() -> Solver:
    s = Solver(2, 3)
    print("create solver instance", s)
    return s


@fixture
def solver_instance2(request) -> Solver:
    print("request.param", request.param)
    a, b = request.param
    s = Solver(a, b)
    return s


class TestSolver:
    def test_add(self, solver_instance):
        # s = Solver(2, 3)
        # s = solver_instance()
        res = solver_instance.add()
        solver_instance.a = 10
        assert res == 5

    def test_mul(self, solver_instance):
        # s = Solver(4, 5)
        # s = solver_instance()
        res = solver_instance.mul()
        assert res == 6

    @mark.parametrize("a, b, expected_result", [
        (1, 2, 2),
        (3, 2, 6),
        param(3, 4, 12),
        param(4, 4, 16, id="some-id"),
        param("abc", 2, "abcabc", id="mul-string"),
    ])
    def test_mul_param1(self, a, b, expected_result):
        s = Solver(a, b)
        res = s.mul()
        assert res == expected_result

    @mark.parametrize("solver_instance2, expected_result", [
        ((1, 2), 2),
        ((3, 2), 6),
        param((3, 4), 12),
        param((4, 4), 16, id="some-id"),
        param(("abc", 2), "abcabc", id="mul-string"),
    ], indirect=["solver_instance2"])
    def test_mul_param2(self, solver_instance2: Solver, expected_result):
        s = solver_instance2
        res = s.mul()
        assert res == expected_result

    @mark.parametrize("solver_instance2", [
        param(["a", "b"]),
    ], indirect=["solver_instance2"])
    def test_mul__raises(self, solver_instance2: Solver):
        with raises(TypeError) as exc_info:
            solver_instance2.mul()

        assert str(exc_info.value) == solver_instance2.EXC_TYPE_ERROR_TEXT
