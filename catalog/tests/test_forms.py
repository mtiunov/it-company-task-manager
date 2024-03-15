from django.contrib.auth import get_user_model
from django.test import TestCase
from catalog.forms import WorkerCreationForm, TaskForm
from catalog.models import TaskType, Position


class FormsTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )

    def test_worker_creation_form_valid(self):
        self.position = Position.objects.create(name="Developer")
        form_data = {
            "username": "test_user",
            "password1": "test123456",
            "password2": "test123456",
            "first_name": "Test_first",
            "last_name": "Test_last",
            "position": self.position,
        }
        form = WorkerCreationForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_task_creation_form_valid(self):
        self.task_type = TaskType.objects.create(name="Bug")
        form_data = {
            "username": "test_user",
            "password1": "test123",
            "password2": "test123",
            "first_name": "Test_first",
            "last_name": "Test_last",
            "task_type": self.task_type.name,
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
