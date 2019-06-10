from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Day, Trip, Location
from . import gmaps

class TripListView(ListView):
    model = Trip
    template_name = "trips-view.html"

    def get_queryset(self):
        return Trip.objects.all()



    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context
