from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('reservations/', views.reservation_list),
    path('reservationcreate/', csrf_exempt(views.reservation_create), name='reservationCreate'),
]