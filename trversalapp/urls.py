from django.urls import path
from . import views

app_name = 'trversal' 
urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('new_trip/', views.TripCreateView.as_view(), name='new-trip'),
    path('<int:pk>/trip/', views.TripDetailView.as_view(), name='view-trip'),
    path('<int:pk>/new_day/', views.DayCreateView.as_view(), name='new-day'),
    path('<int:pk>/day/', views.DayDetailView.as_view(), name='view-day'),
    path('<int:pk>/new_loc/', views.LocCreateView.as_view(), name='new-loc'),
    path('<int:pk>/loc/', views.LocDetailView.as_view(), name='view-loc'),
]