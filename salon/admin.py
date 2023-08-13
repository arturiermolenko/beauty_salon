from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from salon.models import (
    ProcedureType,
    Position,
    Client,
    Procedure,
    Worker
)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    search_fields = ("last_name", "first_name")


@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    search_fields = ("procedure_type__name",)
    list_filter = ("workers__position__name",)


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("position",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "position",
                    )
                },
            ),
        )
    )


admin.site.register(ProcedureType)
admin.site.register(Position)
admin.site.unregister(Group)
