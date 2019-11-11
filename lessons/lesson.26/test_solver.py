from unittest import mock
import pytest



@pytest.fixture('module')
def default_arguments():
    print('default_arguments called')
    return 1, -70, 600


@pytest.fixture
def default_arguments_with_result(default_arguments):
    return default_arguments, (60, 10)

# class TestSquare
def test_solver_module_exists():
    try:
        import solver
    except ModuleNotFoundError:
        # assert False, 'solver module does not exist!'
        pytest.fail('solver module does not exist!')


def test_function_accepts_three_args(default_arguments):
    from solver import square_equation_solver
    try:
        square_equation_solver(*default_arguments)
    except TypeError:
        # assert False, 'function has to take 3 positional arguments'
        pytest.fail('function has to take 3 positional arguments')


def test_square_equation_solver_exists():
    import solver
    assert hasattr(solver, 'square_equation_solver') is True


def test_raises_on_invalid_argument_type():
    from solver import square_equation_solver
    with pytest.raises(TypeError):
        square_equation_solver('1', [2], None)


def test_function_returns_tuple(default_arguments):
    from solver import square_equation_solver
    res = square_equation_solver(*default_arguments)
    assert isinstance(res, tuple)


def test_result_tuple_contains_two_elements(default_arguments):
    from solver import square_equation_solver
    res = square_equation_solver(*default_arguments)
    assert 2 == len(res)


def test_function_solves_right(default_arguments_with_result):
    from solver import square_equation_solver
    res = square_equation_solver(*default_arguments_with_result[0])
    assert default_arguments_with_result[1] == res

#
# def test_function_solves_right_another_equation():
#     from solver import square_equation_solver
#     res = square_equation_solver(1, 6, -7)
#     assert (1, -7) == res
#
#
# def test_equation_d_zero():
#     from solver import square_equation_solver
#     res = square_equation_solver(1, -4, 4)
#     assert (2, None) == res
#
#
# def test_simple_equation():
#     from solver import square_equation_solver
#     res = square_equation_solver(7, 0, 0)
#     assert (0, None) == res
#
#
# def test_a_is_zero():
#     from solver import square_equation_solver
#     res = square_equation_solver(0, 10, 20)
#     assert (-2, None) == res
#
#
# def test_a_is_negative():
#     from solver import square_equation_solver
#     res = square_equation_solver(-10, 20, 30)
#     assert (3, -1) == res
#
#
# def test_a_and_b_are_zeros():
#     from solver import square_equation_solver
#     res = square_equation_solver(0, 0, 42)
#     assert (None, None) == res
#
#
# def test_no_roots():
#     from solver import square_equation_solver
#     res = square_equation_solver(4, 0, 36)
#     assert (None, None) == res


#
#
# @pytest.mark.parametrize(
#     'arguments, expected_result',
#     [
#         ((1, 6, -7), (1, -7)),
#         ((1, -4, 4), (2, None)),
#         ((7, 0, 0), (0, None)),
#         ((0, 10, 20), (-2, None)),
#         ((-10, 20, 30), (3, -1)),
#         ((0, 0, 42), (None, None)),
#         ((4, 0, 36), (None, None)),
#     ],
#     ids=[
#         'function_solves_right_another_equation',
#         'equation_d_zero',
#         'simple_equation',
#         'a_is_zero',
#         'a_is_negative',
#         'a_and_b_are_zeros',
#         'no_roots',
#     ]
# )
# def test_some_cases(arguments, expected_result):
#     from solver import square_equation_solver
#     res = square_equation_solver(*arguments)
#     assert expected_result == res


@pytest.mark.parametrize(
    'arguments, expected_result',
    [
        pytest.param(
            (1, 6, -7), (1, -7),
            id='function_solves_right_another_equation',
        ),
        pytest.param(
            (1, -4, 4), (2, None),
            id='equation_d_zero',
        ),
        pytest.param(
            (7, 0, 0), (0, None),
            id='simple_equation',
        ),
        pytest.param(
            (0, 10, 20), (-2, None),
            id='a_is_zero',
        ),
        pytest.param(
            (-10, 20, 30), (3, -1),
            id='a_is_negative',
        ),
        pytest.param(
            (0, 0, 42), (None, None),
            id='a_and_b_are_zeros',
        ),
        pytest.param(
            (4, 0, 36), (None, None),
            id='no_roots',
        ),
    ],
)
def test_some_cases(arguments, expected_result):
    from solver import square_equation_solver
    res = square_equation_solver(*arguments)
    assert expected_result == res


#

@pytest.fixture
def a_and_its_power_of_two(request):
    a = request.param
    return a, a * a


@pytest.mark.parametrize(
    'a_and_its_power_of_two',
    list(range(10)),
    indirect=['a_and_its_power_of_two']
)
def test_in_power_of_two(a_and_its_power_of_two):
    from solver import in_power_of_two
    a, er = a_and_its_power_of_two
    res = in_power_of_two(a)
    assert er == res


#

@mock.patch('solver.in_power_of_two', autospec=True)
def test_func_uses_power_func(mocked_in_power_of_two):
    from solver import uses_power_func

    b = 42
    res = uses_power_func(b)
    assert res is mocked_in_power_of_two.return_value
    mocked_in_power_of_two.assert_called_once()
    mocked_in_power_of_two.assert_called_once_with(b / 2)
