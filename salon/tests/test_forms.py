import zoneinfo
from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from salon.forms import ProcedureForm
from salon.models import Position, Client, ProcedureType


class FormsTests(TestCase):
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

    def test_procedure_form(self):
        workers_set = get_user_model().objects.filter(username__icontains="test")
        self.procedure_form_data = {
            "procedure_type": self.procedure_type,
            "client": self.client__,
            "date_time": datetime(2023, 12, 9, 14, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
            "is_completed": False,
            "workers": workers_set
        }
        form = ProcedureForm(data=self.procedure_form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.data, self.procedure_form_data)

    def test_procedure_form_has_wrong_date(self):
        workers_set = get_user_model().objects.filter(username__icontains="test")
        self.procedure_form_data = {
            "procedure_type": self.procedure_type,
            "client": self.client__,
            "date_time": datetime(2022, 12, 9, 14, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
            "is_completed": False,
            "workers": workers_set
        }
        form = ProcedureForm(data=self.procedure_form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['date_time'][0], "The date and time cannot be in the past")
