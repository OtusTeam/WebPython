from unittest import TestCase

from helper import get_least


class TestSuccessGetLeast(TestCase):
    def test_success_get_least(self):
        args = [0, 1, 2, 3]
        result = get_least(*args)
        exp_result = 0
        self.assertEqual(result, exp_result)

    def test_success_get_least_2(self):
        args = [-1, 0, 1, 2, 3]
        result = get_least(*args)
        exp_result = 0
        self.assertEqual(result, exp_result)
