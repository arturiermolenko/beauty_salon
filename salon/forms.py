from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils import timezone

from salon.models import Client, Worker, Procedure


class ClientUpdateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ("telephone_number",)


class ClientCreateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


class ProcedureForm(forms.ModelForm):
    workers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    date_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
    )

    def clean_date_time(self):
        date_time = self.cleaned_data.get("date_time")
        if date_time <= timezone.now():
            raise ValidationError("The date and time cannot be in the past")
        return date_time

    class Meta:
        model = Procedure
        fields = "__all__"


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
