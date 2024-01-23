from django.test import TestCase
from .forms import RegistrationForm
from .models import MyUser


class TestRegisterView(TestCase):

    def setUp(self):
        self.response = self.client.get('/users/register/')

    def test_get_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_get_form(self):
        context = self.response.context
        form_context_name = 'form'
        self.assertIn(form_context_name, context)

        form = context[form_context_name]
        self.assertEqual(type(form), RegistrationForm)


class TestRegisterView(TestCase):

    def setUp(self):
        data = {
            'username': 'newuser',
            'email': 'newuser@user.com',
            'password1': 'usernfieuRTopenfenf223h',
            'password2': 'usernfieuRTopenfenf223h',
        }
        self.response = self.client.post('/users/register/', data=data)

    def test_post_status_code(self):
        self.assertEqual(self.response.status_code, 302)

    def test_user_created(self):
        self.assertTrue(MyUser.objects.filter(username='newuser').exists())

    def test_redirect_url(self):
        self.assertRedirects(self.response, '/users/login/')


class TestPermissions(TestCase):

    def test_status_codes(self):
        url = '/category/create/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

        user = MyUser.objects.create_user('user', 'user@user.com', 'user1233455')
        self.client.login(username='user', password='user1233455')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        self.client.logout()

        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

