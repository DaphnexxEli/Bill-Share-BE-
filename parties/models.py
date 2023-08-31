from django.db import models
from menus.models import Restaurant
from users.models import User

TYPE_CHOICES = [
    ('F', 'Food&Drink'),
    ('H', 'Home&Hotel'),
    ('S', 'Subscribe&Service'),
]

# Create your models here.
class Party(models.Model):
    partyName = models.CharField(max_length=30)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, blank=True)
    menu = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, blank=True, null=True)
    hostID = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    Code = models.CharField(max_length=5, unique=True, default='')
    orderList = models.JSONField(default=list, blank=True, null=True)
    timeCreate = models.DateField(auto_now=False, auto_now_add=True)
    promptPay = models.CharField(max_length=10, default='')

class Member(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, default='')
    userID = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='members')
    cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    slipImage = models.ImageField(upload_to='memberslip_images/%Y/%m/%d/', blank=True, null=True)
