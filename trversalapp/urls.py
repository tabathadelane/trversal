from django.urls import path
from . import views

app_name = 'trversal' 
urlpatterns = [
    path('', views.TripListView.as_view(), name='trips')
]