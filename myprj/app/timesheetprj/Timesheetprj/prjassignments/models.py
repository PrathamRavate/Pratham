from django.db import models
from projects.models import Project
from profiles.models import Profile
# Create your models here.
class ProjectAssignment(models.Model):
    Assigned_date =models.DateField()
    Project_name = models.ForeignKey(Project , on_delete=models.CASCADE)
    Employee_id = models.ForeignKey(Profile , on_delete = models.CASCADE)
    Start_date = models.DateTimeField()
    End_date = models.DateTimeField()

