from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model  

from .models import Task, Category

User = get_user_model() 

class TaskModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

        cls.category = Category.objects.create(name='Test Category', user=cls.user)

    def test_task_creation(self):
        task = Task.objects.create(
            title='Test Task',
            description='This is a test task',
            category=self.category,
            user=self.user
        )

        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.description, 'This is a test task')
        self.assertEqual(task.category, self.category)
        self.assertEqual(task.user, self.user)
        self.assertFalse(task.completed)

    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Test Category')
        self.assertEqual(self.category.user, self.user)

