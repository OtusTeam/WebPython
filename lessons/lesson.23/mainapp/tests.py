from django.test import TestCase, SimpleTestCase
from .models import Category, Animal
from mixer.backend.django import mixer

class TestCategory(TestCase):

    def test_some(self):
        self.assertEqual(1, 1)

    def test_str(self):
        category = Category.objects.create(name='some name')
        self.assertEqual(str(category), 'some name')


class TestAnimal(TestCase):

    def test_get_category_name(self):
        # category = mixer.blend(Category, name='some name')
        # animal = mixer.blend(Animal, category=category)

        animal = mixer.blend(Animal, category__name='some name')
        self.assertEqual(animal.get_category_name(), 'some name')


class TestCategoryListView(TestCase):

    def test_status_code(self):
        url = '/category/list/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        url = '/category/list/'
        response = self.client.get(url)
        context = response.context
        self.assertIn('object_list', context)
        category_list = context['object_list']
        self.assertEqual(len(category_list), 0)

        category = Category.objects.create(name='some name')

        response = self.client.get(url)
        context = response.context
        category_list = context['object_list']

        self.assertEqual(len(category_list), 1)

    def test_content(self):
        category = Category.objects.create(name='some name')
        url = '/category/list/'
        response = self.client.get(url)
        content = response.content
        self.assertContains(response, 'some name', 1)