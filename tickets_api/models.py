from email.policy import default
from django.db import models

# Create your models here.
class Ticket(models.Model):
    name = models.CharField(max_length=32)
    venue = models.CharField(max_length=32) 
    date = models.DateField(null=True)
    price = models.IntegerField()
    # image = models.CharField(max_length=100)
    # image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,)



