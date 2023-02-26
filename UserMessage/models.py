from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField(max_length=225, blank=True, null=True)


    