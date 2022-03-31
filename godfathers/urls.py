from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('godfathers/', views.godfather_list),
    path('godfathercreate/', csrf_exempt(views.godfather_create), name='godfatherCreate'),
]