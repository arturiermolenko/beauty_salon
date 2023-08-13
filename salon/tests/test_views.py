import zoneinfo
from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from salon.models import Position, ProcedureType, Client, Procedure, Worker
from salon.views import ClientListView, WorkerListView

PROCEDURE_LIST_URL = reverse("salon:procedure-list")
WORKER_LIST_URL = reverse("salon:worker-list")
CLIENT_LIST_URL = reverse("salon:client-list")


class PrivateProcedureTests(TestCase):
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
        for index in range(1, 11):
            Procedure(
                procedure_type=self.procedure_type,
                client=self.client__,
                date_time=datetime(2023, 12, index, 14, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
                is_completed=False,
            )

    def test_login_required(self):
        response_ = self.client.get(PROCEDURE_LIST_URL)

        self.assertEqual(response_.status_code, 200)

    def test_retrieve_procedures_list(self):
        response_ = self.client.get(PROCEDURE_LIST_URL)
        procedures = Procedure.objects.all()

        self.assertEqual(
            list(response_.context["procedure_list"]),
            list(procedures)
        )
        self.assertTemplateUsed(response_, "salon/procedure_list.html")

    def test_get_queryset(self):
        procedures = Procedure.objects.filter(procedure_type__name__icontains="manicure")
        response_ = self.client.get(PROCEDURE_LIST_URL + "?procedure_type=manicure")

        self.assertEqual(
            list(response_.context["procedure_list"]),
            list(procedures)
        )


class PrivateClientTests(TestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin11",
            password="password11"
        )
        self.client.force_login(self.admin_user)

        for index in range(10):
            Client.objects.create(
                first_name=f"test {index}",
                last_name="test last",
                telephone_number="test tel num"
            )

    def test_login_required(self):
        response_ = self.client.get(CLIENT_LIST_URL)

        self.assertEqual(response_.status_code, 200)

    def test_retrieve_procedures_list(self):
        response_ = self.client.get(CLIENT_LIST_URL)
        clients_ = Client.objects.all()
        pagination = ClientListView.paginate_by

        self.assertEqual(
            list(response_.context["client_list"]),
            list(clients_)[:pagination]
        )
        self.assertTemplateUsed(response_, "salon/client_list.html")

    def test_get_queryset(self):
        clients = Client.objects.filter(last_name__icontains="last")
        response_ = self.client.get(CLIENT_LIST_URL + "?last_name=last")
        pagination = ClientListView.paginate_by

        self.assertEqual(
            list(response_.context["client_list"]),
            list(clients)[:pagination]
        )


class PrivateWorkerTests(TestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin11",
            password="password11"
        )
        self.client.force_login(self.admin_user)

        self.position = Position.objects.create(name="position")
        for index in range(10):
            get_user_model().objects.create_user(
                username=f"test_username_{index}",
                first_name=f"test {index}",
                last_name="test last",
                password="test_pass123",
                position=self.position
            )

    def test_login_required(self):
        response_ = self.client.get(WORKER_LIST_URL)

        self.assertEqual(response_.status_code, 200)

    def test_retrieve_workers_list(self):
        response_ = self.client.get(WORKER_LIST_URL)
        workers = get_user_model().objects.all()
        pagination = WorkerListView.paginate_by

        self.assertEqual(
            list(response_.context["worker_list"]),
            list(workers)[:pagination]
        )
        self.assertTemplateUsed(response_, "salon/worker_list.html")

    def test_get_queryset(self):
        workers = get_user_model().objects.filter(username__icontains="name")
        response_ = self.client.get(WORKER_LIST_URL + "?username=name")
        pagination = WorkerListView.paginate_by

        self.assertEqual(
            list(response_.context["worker_list"]),
            list(workers)[:pagination]
        )
