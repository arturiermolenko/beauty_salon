from django import forms
from django.contrib.auth.forms import UserCreationForm

from salon.models import Client, Worker


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ("telephone_number",)


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "position",
            "first_name",
            "last_name"
        )


class WorkerSearchForm(forms.Form):
    username = forms.CharField(
        required=False,
        max_length=255,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username..."}
        )
    )


class ProcedureSearchForm(forms.Form):
    procedure_type = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by procedure type..."}
        )
    )


class ClientSearchForm(forms.Form):
    last_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by client's last name..."}
        )
    )
