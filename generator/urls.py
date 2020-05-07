from django.urls import path
from generator import views

urlpatterns = [path('generator/', views.generator, name='generator')]
