from unittest import TestCase


class TestSquareEquationSolverTestCase(TestCase):

    def test_solver_module_exists(self):
        try:
            import solver
        except ModuleNotFoundError:
            self.fail('solver module does not exist!')

    def test_square_equation_solver_exists(self):
        import solver
        self.assertTrue(hasattr(solver, 'square_equation_solver'))

    def test_function_accepts_three_args(self):
        from solver import square_equation_solver
        try:
            square_equation_solver(1, -70, 600)
        except TypeError:
            self.fail('function has to take 3 positional arguments')

    def test_raises_on_invalid_argument_type(self):
        from solver import square_equation_solver
        with self.assertRaises(TypeError):
            square_equation_solver('1', [2], None)

    def test_function_returns_tuple(self):
        from solver import square_equation_solver
        res = square_equation_solver(1, -70, 600)
        self.assertIsInstance(res, tuple)

    def test_result_tuple_contains_two_elements(self):
        from solver import square_equation_solver
        res = square_equation_solver(1, -70, 600)
        self.assertEqual(2, len(res))

    def test_function_solves_right(self):
        from solver import square_equation_solver
        res = square_equation_solver(1, -70, 600)
        self.assertEqual((60, 10), res)

    def test_function_solves_right_another_equation(self):
        from solver import square_equation_solver
        res = square_equation_solver(1, 6, -7)
        self.assertEqual((1, -7), res)

    def test_equation_d_zero(self):
        from solver import square_equation_solver
        res = square_equation_solver(1, -4, 4)
        self.assertEqual((2, None), res)

    def test_simple_equation(self):
        from solver import square_equation_solver
        res = square_equation_solver(7, 0, 0)
        self.assertEqual((0, None), res)

    def test_a_is_zero(self):
        from solver import square_equation_solver
        res = square_equation_solver(0, 10, 20)
        self.assertEqual((-2, None), res)

    def test_a_is_negative(self):
        from solver import square_equation_solver
        res = square_equation_solver(-10, 20, 30)
        self.assertEqual((3, -1), res)

    def test_a_and_b_are_zeros(self):
        from solver import square_equation_solver
        res = square_equation_solver(0, 0, 42)
        self.assertEqual((None, None), res)

    def test_no_roots(self):
        from solver import square_equation_solver
        res = square_equation_solver(4, 0, 36)
        self.assertEqual((None, None), res)
