from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('students/', views.student_list, name='studentList'),
    path('studentcreate/$', csrf_exempt(views.student_create), name='studentCreate'),
]