from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path(r'^students/', views.studentList, name='studentList'),
    path('students/', views.student_list, name='student_list'),
    path('studentscreate/', csrf_exempt(views.student_create), name='student_create'),
    path(r'^studentcreate/$', csrf_exempt(views.studentCreate), name='studentCreate'),
]