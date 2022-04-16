from rest_framework import serializers 
from .models import Ticket 

class TicketSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Ticket # tell django which model to use
        fields = ('id', 'name', 'venue', 'event_date', 'price') # tell django which fields to include