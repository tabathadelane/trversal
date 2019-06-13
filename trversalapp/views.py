from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

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
# object level permission use django guardian or other third party or do many to many and check if user

class TripUpdateView(UpdateView):
    model = Trip
    template_name = 'edit_trip.html'
    form_class= NewTripForm.NewTripForm
    # success_url = reverse_lazy('trversal:view-trip')

class TripDetailView(DetailView):
    model = Trip
    template_name = 'view_trip.html'

class TripDeleteView(DeleteView):
    model = Trip
    template_name = 'del_trip.html'
    success_url = reverse_lazy('trversal:index')

class DayCreateView(CreateView):
    model = Day
    template_name = 'new_day.html'
    form_class= NewDayForm.NewDayForm

    def form_valid(self, form):
        form.instance.trip_name = Trip.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)

class DayUpdateView(UpdateView):
    model = Day
    template_name = 'edit_day.html'
    form_class= NewDayForm.NewDayForm
    # success_url = reverse_lazy('trversal:view-day')

class DayDetailView(DetailView):
    model = Day
    template_name = 'view_day.html'

    def get_object(self):
        day = super().get_object()
        gmaps.time_gen(day)
        return day

        # axios vs fetch (vue-too) , send ajax w django
        # build a url with template syntax
        # quote.pk
        # headers
        #lab9 headers csrftoken for header. get element by name=csrftoken.values
        # serialize first
        #use django template for static elements on page, but vue for changing elements. 
        #start with each day as a page with vue list only, later update to seemless browsing with javascript and vue components


class DayDeleteView(DeleteView):
    model = Day
    template_name = 'del_day.html'
    success_url = reverse_lazy('trversal:view-trip')

class LocCreateView(CreateView):
    model = Location
    template_name = 'new_loc.html'
    form_class= NewLocForm.NewLocForm
    # success_url = reverse_lazy('trversal:view-loc')

    def form_valid(self, form):
        form.instance.day = Day.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)

class LocUpdateView(UpdateView):
    model = Location
    template_name = 'edit_loc.html'
    form_class= NewLocForm.NewLocForm
    # success_url = reverse_lazy('trversal:view-loc')

class LocDetailView(DetailView):
    model = Location
    template_name = 'view_loc.html'

class LocDeleteView(DeleteView):
    model = Location
    template_name = 'del_loc.html'
    success_url = reverse_lazy('trversal:view-day')




    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context
