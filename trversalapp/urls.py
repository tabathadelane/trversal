from django.urls import path
from . import views

app_name = 'trversal' 
urlpatterns = [
    path('', views.home, name='home'),

    path('index', views.IndexListView.as_view(), name='index'),
    path('new_trip/', views.TripCreateView.as_view(), name='new-trip'),
    path('<int:pk>/trip/', views.TripDetailView.as_view(), name='view-trip'),
    path('<int:pk>/trip/del', views.TripDeleteView.as_view(), name='del-trip'),
    path('<int:pk>/trip/edit', views.TripUpdateView.as_view(), name='edit-trip'),

    # path('api/trip/<int:pk>', views.tripAPIdetail, name='trip-api'),

    path('<int:pk>/new_day/', views.DayCreateView.as_view(), name='new-day'),
    path('<int:pk>/day/', views.DayDetailView.as_view(), name='view-day'),
    path('<int:pk>/day/del', views.DayDeleteView.as_view(), name='del-day'),
    path('<int:pk>/day/edit', views.DayUpdateView.as_view(), name='edit-day'),

    path('<int:pk>/new_loc/', views.LocCreateView.as_view(), name='new-loc'),
    path('<int:pk>/loc/', views.LocDetailView.as_view(), name='view-loc'),
    path('<int:pk>/loc/del', views.LocDeleteView.as_view(), name='del-loc'),
    path('<int:pk>/loc/edit', views.LocUpdateView.as_view(), name='edit-loc'),
]