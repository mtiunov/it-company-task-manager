from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from catalog.models import Position


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="testadmin"
        )
        self.client.force_login(self.admin_user)
        self.position = Position.objects.create(name="Developer")
        self.worker = get_user_model().objects.create_user(
            username="worker",
            password="testworker",
            position=self.position,
        )

    def test_worker_position_listed(self):
        """
        Test that worker`s position is in list_display
        an worker admin page
        """
        url = reverse("admin:catalog_worker_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.worker.position)

    def test_worker_detail_position_listed(self):
        """
        Test that worker`s position is an worker detail admin page
        """
        url = reverse("admin:catalog_worker_change", args=[self.worker.id])
        res = self.client.get(url)
        self.assertContains(res, self.worker.position)

    def test_worker_add_position_listed(self):
        """
        Test that the worker's position is the admin page
        about adding a worker.
        """
        url = reverse("admin:catalog_worker_add")
        data = {
            "position": "Developer",
        }
        res = self.client.get(url, data)
        self.assertContains(res, data["position"])
