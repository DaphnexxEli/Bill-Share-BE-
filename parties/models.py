from django.db import models

# Create your models here.
class Party(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    menu = models.CharField(max_length=100)
    host = models.CharField(max_length=100)

class Member(models.Model):
    name = models.CharField(max_length=100)
    cost = models.DecimalField(decimal_places=None)