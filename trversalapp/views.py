from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from .models import Day, Trip, Location
from forms import forms
from . import gmaps

def home(request):
	return render(request, 'landing.html')


class IndexListView(ListView):
    model = Trip
    template_name = "index.html"

    def get_queryset(self):
        return Trip.objects.all()

class TripCreateView(CreateView):
    model = Trip
    template_name = 'new_trip.html'
    form_class= forms.NewTripForm
    # success_url = reverse_lazy('trversal:new-day')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
# object level permission use django guardian or other third party or  preferred: do many to many and check if user

class TripUpdateView(UpdateView):
    model = Trip
    template_name = 'edit_trip.html'
    form_class= forms.NewTripForm

    def get_object(self):
        trip = super().get_object()
        num = trip.days.count()
        trip.days_num = num
        trip.save()
        gmaps.reorder_days(trip)
        return trip

class TripDetailView(DetailView):
    model = Trip
    # template_name = 'view_trip.html'
    template_name = 'vue_trip.html'


    # def get_object(self):
    #     trip = super().get_object()
    #     num = trip.days.count()
    #     trip.days_num = num
    #     trip.save()
    #     gmaps.reorder_days(trip)
    #     return trip


class TripDeleteView(DeleteView):
    model = Trip
    template_name = 'del_trip.html'
    success_url = reverse_lazy('trversal:index')

class DayCreateView(CreateView):
    model = Day
    template_name = 'new_day.html'
    form_class= forms.NewDayForm

    def form_valid(self, form):
        form.instance.trip_name = Trip.objects.get(pk=self.kwargs["pk"])
        # form.instance.order = form_trip.days.count() + 1

        return super().form_valid(form)

class DayUpdateView(UpdateView):
    model = Day
    template_name = 'edit_day.html'
    form_class= forms.NewDayForm

class DayDetailView(DetailView):
    model = Day
    # template_name = 'view_day.html'
    template_name = 'vue_day_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = forms.NewLocForm
        return context

    def get_object(self):
        day = super().get_object()
        gmaps.reorder_locs(day)
        gmaps.geocode(day)
        gmaps.date_setter(day)
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

    def get_success_url(self, **kwargs):
            return reverse_lazy('trversal:view-trip', args=(self.object.trip_name.id,))
class LocCreateView(CreateView):
    model = Location
    template_name = 'new_loc.html'
    form_class= forms.NewLocForm

    def get_success_url(self):
      return reverse_lazy('trversal:view-day', args=(self.kwargs["pk"],))

    def form_valid(self, form):
        form_day = Day.objects.get(pk=self.kwargs["pk"])
        form.instance.day = form_day
        form.instance.name = form.instance.g_name.split(",")[0]
        form.instance.order = form_day.locs.count() + 1
        return super().form_valid(form)


class LocUpdateView(UpdateView):
    model = Location
    template_name = 'edit_loc.html'
    form_class= forms.NewLocForm

    def get_success_url(self):
      return reverse_lazy('trversal:view-day', args=(self.object.day.pk,))

    def form_valid(self, form):
        form.instance.name = form.instance.g_name.split(",")[0]
        return super().form_valid(form)

class LocDetailView(DetailView):
    model = Location
    template_name = 'view_loc.html'

class LocDeleteView(DeleteView):
    model = Location
    template_name = 'del_loc.html'
    # success_url = reverse_lazy('trversal:view-day')

    def get_success_url(self, **kwargs):
        return reverse_lazy('trversal:view-day', args=(self.object.day.id,))
        




    # self.request.user.collection_set.all()