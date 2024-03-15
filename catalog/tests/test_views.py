from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from catalog.models import Position, TaskType

POSITION_URL = reverse("catalog:position-list")
TASKTYPE_URL = reverse("catalog:tasktype-list")


class PublicPositionTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(POSITION_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivatePositionTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_retrieve_position(self):
        Position.objects.create(name="Developer")
        response = self.client.get(POSITION_URL)
        self.assertEqual(response.status_code, 200)
        position = Position.objects.all()
        self.assertEqual(
            list(response.context["position_list"]),
            list(position)
        )
        self.assertTemplateUsed(
            response, "catalog/position_list.html"
        )


class PositionSearchTest(TestCase):
    def setUp(self) -> None:
        Position.objects.create(name="Developer")
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_search_position_by_name(self):
        url = reverse("catalog:position-list")
        response = self.client.get(url, {"name": "Developer"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Developer")
        self.assertNotContains(response, "QA")
        response = self.client.get(url, {"name": "a"})
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url, {"name": ""})
        self.assertEqual(response.status_code, 200)


class PositionUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.position = Position.objects.create(
            name="Developer",
        )
        self.url = reverse("catalog:position-update",
                           args=[self.position.id])
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_update_position_by_id(self):
        data = {"name": "Developer"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.position.refresh_from_db()
        self.assertEqual(self.position.name, "Developer")
        self.assertRedirects(response, reverse("catalog:position-list"))


class PositionDeleteViewTest(TestCase):
    def setUp(self) -> None:
        self.position = Position.objects.create(
            name="Developer",
        )
        self.url = reverse("catalog:position-delete",
                           args=[self.position.id])
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_delete_position_by_id(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Position.objects.filter(
            id=self.position.id).exists())
        self.assertRedirects(response, reverse("catalog:position-list"))


class PositionCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.position = Position.objects.create(
            name="Developer",
        )
        self.url = reverse("catalog:position-create")
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_create_position(self):
        url = reverse("catalog:position-list")
        response = self.client.get(url, {"name": "Developer"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Developer")


class PublicTasktypeTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(TASKTYPE_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTasktypeTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_retrieve_tasktype(self):
        TaskType.objects.create(name="Bug")
        response = self.client.get(TASKTYPE_URL)
        self.assertEqual(response.status_code, 200)
        tasktype = TaskType.objects.all()
        self.assertEqual(
            list(response.context["tasktype_list"]),
            list(tasktype)
        )
        self.assertTemplateUsed(
            response, "catalog/tasktype_list.html"
        )


class TaskTypeSearchTest(TestCase):
    def setUp(self) -> None:
        TaskType.objects.create(name="Bug")
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_search_tasktype_by_name(self):
        url = reverse("catalog:tasktype-list")
        response = self.client.get(url, {"name": "Bug"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bug")
        self.assertNotContains(response, "Refactoring")
        response = self.client.get(url, {"name": "a"})
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url, {"name": ""})
        self.assertEqual(response.status_code, 200)


class TasktypeUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.tasktype = TaskType.objects.create(
            name="Bug",
        )
        self.url = reverse("catalog:tasktype-update",
                           args=[self.tasktype.id])
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_update_tasktype_by_id(self):
        data = {"name": "Bug"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.tasktype.refresh_from_db()
        self.assertEqual(self.tasktype.name, "Bug")
        self.assertRedirects(response, reverse("catalog:tasktype-list"))


class TasktypeDeleteViewTest(TestCase):
    def setUp(self) -> None:
        self.tasktype = TaskType.objects.create(
            name="Bug",
        )
        self.url = reverse("catalog:tasktype-delete",
                           args=[self.tasktype.id])
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_delete_tasktype_by_id(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(TaskType.objects.filter(
            id=self.tasktype.id).exists())
        self.assertRedirects(response, reverse("catalog:tasktype-list"))


class TasktypeCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.tasktype = TaskType.objects.create(
            name="Bug",
        )
        self.url = reverse("catalog:tasktype-create")
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_create_tasktype(self):
        url = reverse("catalog:tasktype-list")
        response = self.client.get(url, {"name": "Bug"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bug")
