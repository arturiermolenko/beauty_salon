from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class ProcedureType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    telephone_number = models.CharField(max_length=255)

    class Meta:
        ordering = ["last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.telephone_number}"


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return f"{self.position} - {self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("salon:worker-detail", kwargs={"pk":self.pk})


class Procedure(models.Model):
    procedure_type = models.ForeignKey(ProcedureType, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    additional_info = models.TextField(max_length=500, blank=True)
    date_time = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    workers = models.ManyToManyField(
        Worker,
        related_name="procedures"
    )

    def __str__(self):
        return f"{self.procedure_type.name}: {self.date_time}"
