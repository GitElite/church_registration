from django.db import models

# Create your models here.

class Member(models.Model):
    Surname = models.CharField(default="None", max_length=50)
    Other_name = models.CharField(default="None", max_length=50)
    Phone_number = models.CharField(default="None", max_length=50)
    Date_of_birth = models.DateField(default="None", max_length=50)
    Wedding_anniversary = models.DateField(default="None", max_length=50)
    Missional_Community = models.CharField(default="None", max_length=50)
