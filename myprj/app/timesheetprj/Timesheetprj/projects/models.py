from django.db import models
from profiles.models import Profile
# Create your models here.


class Project(models.Model):
    Project_Name = models.CharField(max_length = 200)
    Work = models.TextField()
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    date = models.DateField()
    employee = models.ForeignKey(Profile, on_delete=models.CASCADE)

    EXECUTION_TYPE = (
        ("ONSITE" , "ONSITE"),
        ("OFFSITE" , "OFFSITE"),
    )
    
    execution_type = models.CharField(max_length=50, choices=EXECUTION_TYPE)





