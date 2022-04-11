import imp
from django.urls import path
from . import views
# file that connects route with view  (controller function)

urlpatterns = [
    path('api/tickets/', views.TicketList.as_view(), name='ticket_list'), 
    path('api/tickets/<int:pk>', views.TicketDetail.as_view(), name='ticket_detail'),  
]

# just adding random edits to save changes 