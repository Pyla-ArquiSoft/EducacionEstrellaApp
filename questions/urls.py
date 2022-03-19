from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('questions/', views.question_list),
    path('questioncreate/', csrf_exempt(views.question_create), name='questionCreate'),
]