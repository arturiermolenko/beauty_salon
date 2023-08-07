from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


def index(request):
    pass


class ProcedureListView(LoginRequiredMixin, generic.ListView):
    pass


class ProcedureCreateView(LoginRequiredMixin, generic.CreateView):
    pass


class ProcedureDetailView(LoginRequiredMixin, generic.DetailView):
    pass


class ProcedureUpdateView(LoginRequiredMixin, generic.UpdateView):
    pass


class ProcedureDeleteView(LoginRequiredMixin, generic.DeleteView):
    pass


class ClientListView(LoginRequiredMixin, generic.ListView):
    pass


class ClientCreateView(LoginRequiredMixin, generic.CreateView):
    pass


class ClientDetailView(LoginRequiredMixin, generic.DetailView):
    pass


class ClientUpdateView(LoginRequiredMixin, generic.UpdateView):
    pass


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
