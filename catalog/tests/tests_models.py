from datetime import datetime
from django.contrib.auth import get_user_model
from django.test import TestCase
from catalog.models import Position, TaskType, Task


class ModelsTests(TestCase):
    def test_position_str(self):
        position = Position.objects.create(
            name="Developer",
        )
        self.assertEqual(str(position),
                         f"{position.name}")

    def test_worker_str(self):
        worker = get_user_model().objects.create(
            username="test",
            password="test123",
            first_name="Bob",
            last_name="Smith",
        )
        self.assertEqual(str(worker),
                         f"{worker.username} ({worker.first_name} "
                         f"{worker.last_name})")

    def test_task_str(self):
        tasktype = TaskType.objects.create(
            name="Bug",
        )
        task = Task.objects.create(
            name="test",
            deadline=datetime(2024, 3, 6),
            task_type=tasktype,
        )
        self.assertEqual(str(task),
                         f"{task.name} ({task.deadline} "
                         f"{task.task_type})")

    def test_tasktype_str(self):
        tasktype = TaskType.objects.create(
            name="Bug",
        )
        self.assertEqual(str(tasktype),
                         f"{tasktype.name}")
