from django.db import models
from django.urls import reverse

from . import choices

class Trip(models.Model):
    name = models.CharField(max_length=100)
    days_num = models.IntegerField(default=1)
    start_day = models.DateField(default="2002-02-22")
    creator = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('trversal:view-trip', args=[str(self.id)])

class Day(models.Model):
    start_time = models.TimeField(max_length=20,default="9:00 AM")
    day_order = models.IntegerField(default=1)
    day_date = models.DateField(null=True, blank=True)
    trip_name = models.ForeignKey("Trip", on_delete=models.CASCADE)

    def __str__(self):
        return (f'Day {self.day_order}')

    def get_absolute_url(self):
        return reverse('trversal:view-day', args=[str(self.id)])

class Location(models.Model):
    g_name = models.TextField(default=" ")
    name = models.TextField(default=" ")
    duration_hour = models.CharField(max_length=20,choices=choices.hour_choices,default=0)
    duration_min = models.CharField(max_length=20,choices=choices.min_choices,default=0)
    route_time = models.TextField(null=True, blank=True)
    time_arr = models.TextField(null=True, blank=True)
    time_leave = models.TextField(null=True, blank=True)
    
    order = models.IntegerField(default=1)
    day = models.ForeignKey("Day", on_delete=models.CASCADE)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('trversal:view-loc', args=[str(self.id)])