from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from salon.forms import (
    ProcedureSearchForm,
    ClientSearchForm,
    WorkerSearchForm,
    WorkerCreationForm,
    ClientCreateForm,
    ClientUpdateForm,
    ProcedureForm
)
from salon.models import Client, Worker, Procedure


class IndexView(generic.TemplateView):
    template_name = "salon/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        num_clients = Client.objects.count()
        num_workers = Worker.objects.count()
        num_procedures = Procedure.objects.count()

        num_visits = self.request.session.get("num_visits", 0)
        self.request.session["num_visits"] = num_visits + 1

        context["num_clients"] = num_clients
        context["num_workers"] = num_workers
        context["num_procedures"] = num_procedures
        context["num_visits"] = num_visits + 1

        return context


class ProcedureListView(LoginRequiredMixin, generic.ListView):
    model = Procedure
    context_object_name = "procedure_list"
    template_name = "salon/procedure_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProcedureListView, self).get_context_data(**kwargs)

        procedure_type = self.request.GET.get("procedure_type", "")

        context["search_form"] = ProcedureSearchForm(
            initial={"procedure_type": procedure_type}
        )

        return context

    def get_queryset(self):
        queryset = (Procedure.objects.
                    prefetch_related("workers").
                    select_related("procedure_type").
                    select_related("client"))
        form = ProcedureSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                procedure_type__name__icontains=(
                    form.cleaned_data["procedure_type"]
                )
            )

        return queryset


class ProcedureCreateView(LoginRequiredMixin, generic.CreateView):
    model = Procedure
    form_class = ProcedureForm
    success_url = reverse_lazy("salon:procedure-list")


class ProcedureUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Procedure
    form_class = ProcedureForm
    success_url = reverse_lazy("salon:procedure-list")


class ProcedureDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Procedure
    success_url = reverse_lazy("salon:procedure-list")


class ClientListView(LoginRequiredMixin, generic.ListView):
    model = Client
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ClientListView, self).get_context_data(**kwargs)

        last_name = self.request.GET.get("last_name", "")

        context["search_form"] = ClientSearchForm(
            initial={"last_name": last_name}
        )

        return context

    def get_queryset(self):
        queryset = Client.objects.all()
        form = ClientSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                last_name__icontains=form.cleaned_data["last_name"]
            )

        return queryset


class ClientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Client
    form_class = ClientCreateForm
    success_url = reverse_lazy("salon:client-list")


class ClientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Client


class ClientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Client
    form_class = ClientUpdateForm
    success_url = reverse_lazy("salon:client-list")


class ClientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Client
    success_url = reverse_lazy("salon:client-list")


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)

        username = self.request.GET.get("username", "")

        context["search_form"] = WorkerSearchForm(
            initial={"username": username}
        )

        return context

    def get_queryset(self):
        queryset = Worker.objects.select_related("position")
        form = WorkerSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    queryset = Worker.objects.prefetch_related("procedures__workers")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerCreationForm


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("salon:worker-list")
