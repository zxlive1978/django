from django.urls import path
from . import views

urlpatterns = [
    path('', views.tech_list, name='tech_list'),

]
