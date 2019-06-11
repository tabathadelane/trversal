from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView

from .models import Day, Trip, Location
from forms import NewTripForm, NewDayForm, NewLocForm
from . import gmaps

class IndexListView(ListView):
    model = Trip
    template_name = "index.html"

    def get_queryset(self):
        return Trip.objects.all()

class TripCreateView(CreateView):
    model = Trip
    template_name = 'new_trip.html'
    form_class= NewTripForm.NewTripForm
    # success_url = reverse_lazy('trversal:new-day')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class TripDetailView(DetailView):
    model = Trip
    template_name = 'view_trip.html'

class DayCreateView(CreateView):
    model = Day
    template_name = 'new_day.html'
    form_class= NewDayForm.NewDayForm
    # success_url = reverse_lazy('trversal:new-loc')

    def form_valid(self, form):
        form.instance.trip_name = Trip.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)

class DayDetailView(DetailView):
    model = Day
    template_name = 'view_day.html'

class LocCreateView(CreateView):
    model = Location
    template_name = 'new_loc.html'
    form_class= NewLocForm.NewLocForm
    success_url = reverse_lazy('trversal:new-loc')

class LocDetailView(DetailView):
    model = Location
    template_name = 'view_loc.html'


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context
