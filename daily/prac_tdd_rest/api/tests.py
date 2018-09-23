from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Todo


class ModelTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='tester')
        self.title = 'write test code'
        self.todo = Todo(title=self.title, owner=user)

    def test_model_can_create_a_todo(self):
        old_count = Todo.objects.count()
        self.todo.save()
        new_count = Todo.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='view_tester')
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.todo_data = {'title':'view test', 'owner':user.id}
        self.response = self.client.post(
                reverse('create'),
                self.todo_data,
                format='json')

    def test_api_can_create_a_todo(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_todo(self):
        todo = Todo.objects.get()
        response = self.client.get(
                '/todolist/', kwargs={'pk':todo.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, todo)

    def test_api_can_update_a_todo(self):
        todo = Todo.objects.get()
        change_data = {'title':'update test'}
        res = self.client.put(
                reverse('details', kwargs={'pk':todo.id}),
                change_data,
                format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_a_todo(self):
        todo = Todo.objects.get()
        response = self.client.delete(
                reverse('details', kwargs={'pk':todo.id}),
                format='json', follow=True)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
