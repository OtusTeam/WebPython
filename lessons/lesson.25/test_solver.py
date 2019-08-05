from unittest import TestCase


class SquareEquationSolverTestCase(TestCase):

    def test_solver_module_exists(self):
        try:
            import solver
        except ModuleNotFoundError:
            self.fail('Module solver not found')

    def test_solver_function_exists(self):
        import solver
        self.assertTrue(
            hasattr(solver, 'square_equation_solver')
        )

    def test_function_accepts_args(self):
        from solver import square_equation_solver
        try:
            square_equation_solver(1, -70, 600)
        except TypeError:
            self.fail('Function must take 3 args')

    def test_raises_on_invalid_argument_type(self):
        from solver import square_equation_solver
        with self.assertRaises(TypeError):
            square_equation_solver('1', [-70], None)

    def test_function_returns_tuple(self):
        from solver import square_equation_solver
        result = square_equation_solver(1, -70, 600)
        self.assertIsInstance(result, tuple)

    def test_function_returns_tuple_with_two_elements(self):
        from solver import square_equation_solver
        result = square_equation_solver(1, -70, 600)
        self.assertEqual(len(result), 2)

    def test_function_solved_equation_right(self):
        from solver import square_equation_solver
        result = square_equation_solver(1, -70, 600)
        self.assertEqual(result, (60, 10))

    def test_function_solved_another_equation_right_and_returns_max_first(self):
        from solver import square_equation_solver
        result = square_equation_solver(1, 10, -24)
        self.assertEqual(result, (2, -12))

    def test_another_equation(self):
        from solver import square_equation_solver
        result = square_equation_solver(1, 3, 2)
        self.assertEqual(result, (-1, -2))

    def test_d_equals_zero(self):
        from solver import square_equation_solver
        result = square_equation_solver(3, -18, 27)
        self.assertEqual(result, (3, None))

    def test_simple_square_equation(self):
        from solver import square_equation_solver
        result = square_equation_solver(5, 0, 0)
        self.assertEqual(result, (0, None))

    def test_a_is_zero(self):
        from solver import square_equation_solver
        result = square_equation_solver(0, 10, 20)
        self.assertEqual(result, (-2, None))

    def test_a_and_b_are_zeros(self):
        from solver import square_equation_solver
        result = square_equation_solver(0, 0, 42)
        self.assertEqual(result, (None, None))

    def test_float_result(self):
        from solver import square_equation_solver
        x1, x2 = square_equation_solver(1, 5, 3)
        self.assertEqual(-0.6972243622680054, x1)
        self.assertEqual(-4.302775637731995, x2)
