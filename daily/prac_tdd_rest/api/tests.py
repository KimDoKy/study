from django.test import TestCase
from .models import Todo


class ModelTestCase(TestCase):

    def setUp(self):
        self.title = 'write test code'
        self.todo = Todo(title=self.title)

    def test_model_can_a_todo(self):
        old_count = Todo.objects.count()
        self.todo.save()
        new_count = Todo.objects.count()
        self.assertNotEqual(old_count, new_count)
