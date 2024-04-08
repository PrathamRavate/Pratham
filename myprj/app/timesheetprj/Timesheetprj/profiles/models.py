from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    DEPARTMENT_CHOICES = (
        ("SAC", "SAC"),
        ("Engineering", "Engineering"),
        ("SAP_SD", "SAP_SD"),
        ("SAP_PP", "SAP_PP"),
        ("SAP_MM", "SAP_MM"),
        ("SAP_FICO", "SAP_FICO"),
        ("SAP_ABAP", "SAP_ABAP"),
    )
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)

    ROLE_CHOICES = (
        ("Trainee", "Trainee"),
        ("Associate", "Associate"),
        ("Consultant", "Consultant"),
        ("Senior Associate", "Senior Associate"),
        ("Manager", "Manager"),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    def __str__(self):
        return self.name
