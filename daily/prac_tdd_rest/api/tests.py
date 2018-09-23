from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Todo


class ModelTestCase(TestCase):

    def setUp(self):
        self.title = 'write test code'
        self.todo = Todo(title=self.title)

    def test_model_can_create_a_todo(self):
        old_count = Todo.objects.count()
        self.todo.save()
        new_count = Todo.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.todo_data = {'title':'view test'}
        self.response = self.client.post(
                reverse('create'),
                self.todo_data,
                format='json')

    def test_api_can_create_a_todo(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
