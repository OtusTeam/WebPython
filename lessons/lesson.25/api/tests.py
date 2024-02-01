import json
from rest_framework.test import APITestCase, APISimpleTestCase, APIClient
from userapp.models import MyUser
from django.contrib.auth.models import Group, Permission
import random
import unittest.mock as mock


class CategoryViewSetTestCase(APITestCase):

    @classmethod
    def setUpClass(cls):
        print(
            'I run only once'
        )
        super().setUpClass()


    def setUp(self):
        self.url = '/api/viewsets/category/'
        self.auth_client = APIClient()
        self.user = MyUser.objects.create_user('user' 'user@user.com', 'user123456')
        self.auth_client.force_authenticate(user=self.user)

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 401)
        response = self.auth_client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'], [])
        self.assertTrue(isinstance(response.content, bytes))

    def test_create(self):
        # print('создание группы "Учителя" (Teachers)')
        test_group, _ = Group.objects.get_or_create(name='Test group')
        perm = Permission.objects.filter(codename='add_category')
        test_group.permissions.set(perm)

        test_group.user_set.add(
            self.user
        )

        data = {
            'name': 'Test category'
        }

        response = self.auth_client.post(self.url, data=data)
        self.assertEqual(response.status_code, 201)
        # How to check create data?
        # self.assertEqual(response.data, {'name': 'Test category'})


class RandomTestCase(APISimpleTestCase):

    def setUp(self):
        self.url = '/api/views/random/'


    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_data(self):

        def random_mock(a, b):
            return 0

        #old_random = random.randint

        #random.randint = random_mock
        with mock.patch('random.randint', random_mock):
            response = self.client.get(self.url)
            random_number = response.data['random_number']
            # self.assertIn(random_number, [1, 2])
            self.assertEqual(random_number, 0)

        with mock.patch('random.randint') as random_value:
            random_value.return_value = 0
            response = self.client.get(self.url)
            random_number = response.data['random_number']
            # self.assertIn(random_number, [1, 2])
            self.assertEqual(random_number, 0)

        #random.randint = old_random
