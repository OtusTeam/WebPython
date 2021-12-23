import pytest
from django.contrib.auth import get_user_model
from django.core import mail
from django.test import TestCase


@pytest.mark.django_db
class OtusUserTests(TestCase):
    fixtures = ['myauth.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_model = get_user_model()

    def test_login_user(self):
        response = self.client.get('/')
        # print(dir(response))
        # print(response.content)
        # print(response.context)
        assert response.context['user'].is_anonymous

        response = self.client.post(
            '/myauth/user/login/',
            data={'username': 'user1', 'password': 'OtusOtus'}
        )
        assert response.status_code == 302

        response = self.client.get('/')
        assert not response.context['user'].is_anonymous

    def test_login_user_adv(self):
        response = self.client.get('/')
        assert response.context['user'].is_anonymous

        self.client.login(
            **{'username': 'user1', 'password': 'OtusOtus'}
        )

        response = self.client.get('/')
        assert not response.context['user'].is_anonymous

    def test_create_wrong_user(self):
        with pytest.raises(TypeError):
            self.user_model.objects.create_user()
        with pytest.raises(TypeError):
            self.user_model.objects.create_user(email='')
        with pytest.raises(TypeError):
            self.user_model.objects.create_user(
                first_name='Someone',
                email='', password='pass'
            )

    def test_create_superuser(self):
        self.admin_user = self.user_model.objects.create_superuser(
            first_name='SuperAdmin',
            email='admin@otus.com',
            username='admin',
            password='pass'
        )

        assert self.admin_user.email == 'admin@otus.com'
        assert self.admin_user.is_active
        assert self.admin_user.is_staff
        assert self.admin_user.is_superuser

    def test_create_wrong_superuser(self):
        with pytest.raises(TypeError):
            self.user_model.objects.create_superuser(
                first_name='Super1',
                email='', password='pass')

    def test_send_mail_to_user(self):
        custom_user = self.user_model.objects.create(
            first_name='user55',
            email='user55@otus.ru',
            username='user55',
            password='pass'
        )

        custom_user.email_user(
            'Hello from Otus',
            'You are invited to our party',
            'noreply@otus.com',
            fail_silently=False
        )
        assert len(mail.outbox) == 1
        assert mail.outbox[0].subject == 'Hello from Otus'
        assert mail.outbox[0].body == 'You are invited to our party'
        assert mail.outbox[0].from_email == 'noreply@otus.com'
        assert mail.outbox[0].to == [custom_user.email]

    def test_register_user(self):
        response = self.client.post(
            '/myauth/user/create/',
            data={
                'username': 'user21',
                'password1': 'OtusOtus',
                'password2': 'OtusOtus',
                'email': 'user21@otus.local',
            }
        )
        assert response.status_code == 302

        new_user = self.user_model.objects.get(username='user21')
        assert new_user.email == 'user21@otus.local'

    def test_register_user_error_1(self):
        response = self.client.post(
            '/myauth/user/create/',
            data={
                'username': 'user21',
                'password1': 'OtusOtus',
                'password2': 'OtusOtus',
                # 'email': 'user21@otus.local',
            }
        )
        assert response.status_code == 200

        self.assertFormError(response, 'form', 'email', 'This field is required.')
        # print(response.content)
