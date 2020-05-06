from django.urls import path
from decoder import views

urlpatterns = [path('', views.index, name='home')]
