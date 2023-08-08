from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from salon.forms import (
    ProcedureSearchForm,
    ClientSearchForm, ClientForm
)
from salon.models import Client, Worker, Procedure


def index(request):
    """View function for the home page of the site."""
    num_clients = Client.objects.count()
    num_workers = Worker.objects.count()
    num_procedures = Procedure.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_clients": num_clients,
        "num_workers": num_workers,
        "num_procedures": num_procedures,
        "num_visits": num_visits + 1,
    }

    return render(request, "salon/index.html", context=context)


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
        queryset = Procedure.objects.select_related("procedure_type")
        form = ProcedureSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                procedure_type__name__icontains=form.cleaned_data["procedure_type"]
            )

        return queryset


class ProcedureCreateView(LoginRequiredMixin, generic.CreateView):
    model = Procedure
    fields = "__all__"
    success_url = reverse_lazy("salon:procedure-list")


class ProcedureDetailView(LoginRequiredMixin, generic.DetailView):
    model = Procedure
    success_url = reverse_lazy("salon:procedure-list")


class ProcedureUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Procedure
    fields = "__all__"
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
    form_class = ClientForm
    success_url = reverse_lazy("salon:client-list")


class ClientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Client


class ClientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("salon:client-list")


class ClientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Client
    success_url = reverse_lazy("salon:client-list")


class WorkerListView(LoginRequiredMixin, generic.ListView):
    pass


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    pass


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    pass


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    pass


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    pass


class ClientDeleteView(LoginRequiredMixin, generic.DeleteView):
    pass
