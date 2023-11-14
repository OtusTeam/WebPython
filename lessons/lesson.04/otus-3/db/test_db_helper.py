import unittest

from db_helper import User


# class UserTest(unittest.TestCase):
#     def test_init(self):
#         username = 'Otus'
#         user = User(username=username)
#         self.assertEqual(user.username, username)
#
#     def test_str(self):
#         username = 'Otus'
#         user = User(username=username)
#         self.assertEqual(str(user), username)
#
#     def test_delete(self):
#         username = 'Otus'
#         user = User(username=username)
#         self.assertTrue(user.delete())


class UserTest(unittest.TestCase):
    # def setUp(self):
    #     print('setUp')
    #     self.username = 'Otus'
    #     self.user = User(username=self.username)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        print('setUp')
        cls.username = 'Otus'
        cls.user = User(username=cls.username)

    def test_init(self):
        self.assertEqual(self.user.username, self.username)

    def test_str(self):
        self.assertEqual(str(self.user), self.username)

    def test_delete(self):
        self.assertTrue(self.user.delete())
