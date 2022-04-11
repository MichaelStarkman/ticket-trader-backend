from rest_framework import generics
from .serializers import TicketSerializer
from .models import Ticket

class TicketList(generics.ListCreateAPIView):
    queryset = Ticket.objects.all().order_by('id') 
    serializer_class = TicketSerializer 

class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all().order_by('id')
    serializer_class = TicketSerializer