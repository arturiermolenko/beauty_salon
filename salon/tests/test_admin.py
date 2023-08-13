from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from salon.models import Position


class AdminTests(TestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin11",
            password="password11"
        )
        self.client.force_login(self.admin_user)

        self.position = Position.objects.create(
            name="manicurist"
        )

        self.worker = get_user_model().objects.create_user(
            username="testusername",
            first_name="test first",
            last_name="test last",
            password="test1234",
            position=self.position
        )

    def test_position_listed(self):
        url = reverse("admin:salon_worker_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.worker.position)

    def test_position_in_fieldsets(self):
        url = "http://127.0.0.1:8000/admin/salon/worker/1/change/"
        response = self.client.get(url)

        self.assertContains(response, "position")

    def test_position_in_add_fieldsets(self):
        url = reverse("admin:salon_worker_add")
        response = self.client.get(url)

        self.assertContains(response, "first_name")
        self.assertContains(response, "last_name")
        self.assertContains(response, "position")
