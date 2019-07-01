"""trversal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'trips', views.TripViewSet)
router.register(r'days', views.DayViewSet)
router.register(r'locs', views.LocViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('trversal/user/', include('users.urls')),
    path('trversal/', include('trversalapp.urls')),
    path('api/recalc/days/<int:pk>/', views.ReCalcDay.as_view()),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('test', TemplateView.as_view(template_name="api_test_js.html")),
    path('test2/<int:pk>/', views.LocDetail.as_view()),

]
