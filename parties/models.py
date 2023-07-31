from django.db import models
from menus.models import Restaurant

# Create your models here.
class Party(models.Model):
    partyName = models.CharField(max_length=30)
    type = models.CharField(max_length=100)
    menu = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True, null=True)
    host = models.CharField(max_length=100, default="")
    Code = models.CharField(max_length=5, unique=True, default='')
    orderList = models.JSONField(blank=True, null=True)

class Member(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)
