from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('', views.home, name='home'),
    path('userlist', views.UserListView.as_view(), name='user_list'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<str:username>/edit/', views.SignUpView.as_view(), name='edit-user'),
    path('<str:username>/', views.MyTripList.as_view(), name='mytrip_list'),
]