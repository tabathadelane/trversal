from django.db import models
from django.urls import reverse

from . import choices

class Trip(models.Model):
    trip_name = models.CharField(max_length=100)
    days_num = models.IntegerField(default=1)
    start_day = models.DateField(default="2002-02-22")
    creator = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.trip_name
    
    def get_absolute_url(self):
        return reverse('trversal:view-trip', args=[str(self.id)])

class Day(models.Model):
    start_time = models.TimeField(default="9:00 AM")
    day_date = models.IntegerField(default=1)
    trip_name = models.ForeignKey("Trip", on_delete=models.CASCADE)

    def __str__(self):
        return (f'Day {self.day_date}')

    def get_absolute_url(self):
        return reverse('trversal:view-day', args=[str(self.id)])

class Location(models.Model):
    name = models.TextField(default=" ")
    duration_hour = models.CharField(max_length=20,choices=choices.hour_choices,default=None)
    duration_min = models.CharField(max_length=20,choices=choices.min_choices,default=None)
    route_time = models.TextField(null=True, blank=True)
    order = models.IntegerField(default=1)
    day = models.ForeignKey("Day", on_delete=models.CASCADE)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('trversal:view-loc', args=[str(self.id)])