from django.db import models

# Create your models here.
from profiles.models import Profile
from projects.models import Project



class Ticket(models.Model):
    title = models.TextField(max_length=50)
    description = models.TextField(max_length=50)
    issuedate = models.DateTimeField()
    duedate = models.DateTimeField()
 
    STATUS = (
        ("REGISTER", "REGISTER"),
        ("APPROVED", "APPROVED"),
        ("REJECTED", "REJECTED"),
    )
    status = models.CharField(max_length = 50 , choices = STATUS)

    PRIORITY_CHOICES = (
        ("LOW" , "LOW"),
        ("MEDIUM" , "MEDIUM"),
        ("HIGH" , "HIGH"),
        ("SHOW_STOPPER" , "SHOW_STOPPER"),
    
    )
    priority_choices = models.CharField(max_length = 50 , choices = PRIORITY_CHOICES)
    employee = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    MODULE_CHOICES = (
        ("SAP SD", "SAP SD"),
        ("SAP PP","SAP PP"),
        ("SAP MM", "SAP MM"),
        ("SAP FICO", "SAP FICO"),
        ("SAP ABAP", "SAP ABAP"),
    )
    module = models.CharField(max_length = 50 , choices = MODULE_CHOICES)