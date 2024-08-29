from django.test import TestCase
from django.utils import timezone
from .models import TestModel

class BaseModelTestCase(TestCase):
    
    def setUp(self):
        self.test_instance = TestModel.objects.create(name="Test Instance")

    def test_created_at(self):
 
        self.assertIsNotNone(self.test_instance.created_at)
        self.assertTrue(self.test_instance.created_at <= timezone.now())

    def test_updated_at(self):

        initial_updated_at = self.test_instance.updated_at
        self.assertIsNotNone(initial_updated_at)
        self.assertTrue(initial_updated_at <= timezone.now())

        self.test_instance.name = "Updated Test Instance"
        self.test_instance.save()

        self.test_instance.refresh_from_db()
        self.assertTrue(self.test_instance.updated_at > initial_updated_at)