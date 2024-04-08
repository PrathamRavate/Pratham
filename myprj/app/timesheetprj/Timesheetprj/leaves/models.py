from django.db import models
from profiles.models import Profile

# Create your models here.

class Leave(models.Model):

    LEAVETYPE_CHOICES = (
        ("EARNED_LEAVE" , "EARNED_LEAVE"),
        ("CASUAL_LEAVE" , "CASUAL_LEAVE"),
        ("SICK_LEAVE" , "SICK_LEAVE"),
    )

    leave_type = models.CharField(max_length=50 , choices = LEAVETYPE_CHOICES)
    employee = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    startdate = models.DateField()
    enddate = models.DateField()

    STATUS = (
        ("REGISTER", "REGISTER"),
        ("APPROVED", "APPROVED"),
        ("REJECTED", "REJECTED"),
    )

    status = models.CharField(max_length = 50 , choices = STATUS)