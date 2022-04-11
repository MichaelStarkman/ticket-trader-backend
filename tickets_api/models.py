from django.db import models

# Create your models here.
class Ticket(models.Model):
    name = models.CharField(max_length=32)
    venue = models.CharField(max_length=32) 
    # consider adding min_length=2 
    # date = models.DateTimeField
    price = models.IntegerField()
    #    img(Str)