from django.db import models

# Create your models here.
from profiles.models import Profile
from projects.models import Project
    
class Event(models.Model):
    Description = models.TextField(max_length = 255)
    date = models.DateField()
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    employee = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    STATUS = (
        ("REGISTERD" , "REGISTERD"),
        ("APPROVED", "APPROVED"),
        ("REJECTED", "REJECTED"),
    )

    status = models.CharField(max_length = 50 , choices = STATUS)