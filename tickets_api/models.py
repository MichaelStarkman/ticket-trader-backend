from email.policy import default
from django.db import models

# Create your models here.
class Ticket(models.Model):
    name = models.CharField(max_length=32)
    venue = models.CharField(max_length=32) 
    event_date = models.DateField(null=True)
    price = models.IntegerField()
    img = models.CharField(null=True, max_length=100)
    # img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,)



