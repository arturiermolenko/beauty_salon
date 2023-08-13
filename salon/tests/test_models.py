import zoneinfo
from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from salon.models import Position, ProcedureType, Client, Procedure


class ModelTests(TestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin11",
            password="password11"
        )
        self.client.force_login(self.admin_user)

        self.position = Position.objects.create(
            name="manicurist"
        )

        self.procedure_type = ProcedureType.objects.create(
            name="manicure"
        )
        self.client__ = Client.objects.create(
            first_name="test name",
            last_name="test last",
            telephone_number="test tel num"
        )

        self.worker = get_user_model().objects.create_user(
            username="testusername",
            first_name="test first",
            last_name="test last",
            password="test1234",
            position=self.position
        )
        self.procedure = Procedure(
            procedure_type=self.procedure_type,
            client=self.client__,
            date_time=datetime(2023, 12, 9, 14, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
            is_completed=False,
        )

    def test_procedure_type_str(self):
        self.assertEqual(
            str(self.procedure_type),
            self.procedure_type.name.title()
        )

    def test_client_str(self):
        self.assertEqual(
            str(self.client__),
            f"{self.client__.first_name} "
            f"{self.client__.last_name} - {self.client__.telephone_number}"
        )

    def test_position_str(self):
        self.assertEqual(
            str(self.position),
            self.position.name.title()
        )

    def test_worker_str(self):
        self.assertEqual(
            str(self.worker),
            f"{self.worker.position} - {self.worker.first_name} {self.worker.last_name}"
        )

    def test_procedure_str(self):
        self.assertEqual(
            str(self.procedure),
            f"{self.procedure.procedure_type.name}: {self.procedure.date_time}"
        )

    def test_worker_get_absolute_url(self):
        url = self.worker.get_absolute_url()
        absolute_url = f"/workers/{self.worker.pk}/"
        self.assertEqual(url, absolute_url)