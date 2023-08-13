from django.urls import path

from salon.views import (
    index,
    ProcedureListView,
    ProcedureCreateView,
    ProcedureUpdateView,
    ProcedureDeleteView,
    ClientListView,
    ClientCreateView,
    ClientDetailView,
    ClientUpdateView,
    ClientDeleteView,
    WorkerListView,
    WorkerCreateView,
    WorkerDetailView,
    WorkerUpdateView,
    WorkerDeleteView
)

urlpatterns = [
    path("", index, name="index"),
    path("procedures/", ProcedureListView.as_view(), name="procedure-list"),
    path(
        "procedures/create/",
        ProcedureCreateView.as_view(),
        name="procedure-create"
    ),
    path(
        "procedures/<int:pk>/update/",
        ProcedureUpdateView.as_view(),
        name="procedure-update"
    ),
    path(
        "procedures/<int:pk>/delete",
        ProcedureDeleteView.as_view(),
        name="procedure-delete"
    ),
    path("clients/", ClientListView.as_view(), name="client-list"),
    path("clients/create/", ClientCreateView.as_view(), name="client-create"),
    path(
        "clients/<int:pk>/",
        ClientDetailView.as_view(),
        name="client-detail"
    ),
    path(
        "clients/<int:pk>/update",
        ClientUpdateView.as_view(),
        name="client-update"
    ),
    path(
        "clients/<int:pk>/delete/",
        ClientDeleteView.as_view(),
        name="client-delete"
    ),
    path("workers", WorkerListView.as_view(), name="worker-list"),
    path(
        "workers/create/",
        WorkerCreateView.as_view(),
        name="worker-create"
    ),
    path(
        "workers/<int:pk>/",
        WorkerDetailView.as_view(),
        name="worker-detail"
    ),
    path(
        "workers/<int:pk>/update/",
        WorkerUpdateView.as_view(),
        name="worker-update"
    ),
    path(
        "workers/<int:pk>/delete/",
        WorkerDeleteView.as_view(),
        name="worker-delete"
    ),
]

app_name = "salon"
