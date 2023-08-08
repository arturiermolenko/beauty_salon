from django import forms

from salon.models import Client


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = "__all__"


class ProcedureSearchForm(forms.ModelForm):
    procedure_type = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by procedure type..."}
        )
    )


class ClientSearchForm(forms.ModelForm):
    last_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by client's last name..."}
        )
    )
