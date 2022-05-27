from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('answers/', views.answer_list),
    path('answercreate/', csrf_exempt(views.answer_create), name='answercreate'),
]