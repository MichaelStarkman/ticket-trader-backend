from email.policy import default
from django.db import models
from django.db.models import Model


# Create your models here.
class Ticket(models.Model):
    name = models.CharField(max_length=32)
    venue = models.CharField(max_length=32) 
    event_date = models.DateField(null=True)
    price = models.IntegerField()
    # img = models.CharField(null=True, max_length=100)
    # img = models.ImageField()



