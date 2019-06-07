from django.urls import path
from . import views

app_name = 'trversal' 
urlpatterns = [
    path('', views.HomeView, name='home')
]