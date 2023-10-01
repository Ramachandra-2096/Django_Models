from django.db import models

class Employee(models.Model):
    fullname = models.CharField(max_length=30)
    mobile = models.IntegerField()
