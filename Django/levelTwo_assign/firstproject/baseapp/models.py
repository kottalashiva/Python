from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=250)
    lname = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
