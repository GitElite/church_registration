from django.db import models

# Create your models here.

class Member(models.Model):
    Missional_Community = models.CharField(default="None", max_length=50)
    Date_of_birth = models.CharField(default="None", max_length=50)
    Work_place = models.CharField(default="None", max_length=50)
    Place_of_residence = models.CharField(default="None", max_length=50)
    Whatsapp_phone_number = models.CharField(default="None", max_length=50)
    Primary_phone_number = models.CharField(default="None", max_length=50)
    Other_name = models.CharField(default="None", max_length=50)
    Surname = models.CharField(default="None", max_length=50)
