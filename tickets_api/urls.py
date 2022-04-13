from django.urls import path
from . import views
# file that connects route with view  (controller function)

urlpatterns = [
    path('', views.TicketList.as_view(), name='ticket_list'), 
    path('<int:pk>', views.TicketDetail.as_view(), name='ticket_detail'),  
]
