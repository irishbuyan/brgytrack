from django.db import models
from django.contrib.auth.models import User

class Resident(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Blotter(models.Model):
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    complaint = models.TextField()
    case_number = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return self.case_number


class Certificate(models.Model):
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    certificate_type = models.CharField(max_length=100)
    issued_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.certificate_type


class Report(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title