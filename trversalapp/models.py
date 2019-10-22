from django.db import models
from django.urls import reverse, reverse_lazy

from datetime import datetime as dt



from . import choices

class Trip(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.TimeField(max_length=20,default="9:00 AM")
    creator = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    mode = models.CharField(max_length=20,choices=choices.travel_choices,default="DRIVING")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('trversal:edit-trip', args=[str(self.id)])

    @property
    def past_trip(self):
        # return self.start_day > dt.today()
        return dt.strptime(str(self.date), "%Y-%m-%d") < dt.today()


# class Day(models.Model):
#     day_order = models.IntegerField(default=1)
#     trip_name = models.ForeignKey("Trip", related_name="days", on_delete=models.CASCADE)

    

#     def __str__(self):
#         return (f'Day {self.day_order}')

#     def get_absolute_url(self):
#         return reverse('trversal:view-trip', args=[str(self.trip_name.pk)])
#         # return reverse('trversal:view-day', args=[str(self.id)])

class Location(models.Model):
    g_name = models.TextField(max_length=250,default=" ")
    g_lat = models.FloatField(null=True, blank=True)
    g_lng= models.FloatField(null=True, blank=True)
    name = models.TextField(default=" ")
    duration_hour = models.CharField(max_length=20,choices=choices.hour_choices,default="1")
    duration_min = models.CharField(max_length=20,choices=choices.min_choices,default="15")
    route_time = models.TextField(null=True, blank=True)
    time_arr = models.TextField(null=True, blank=True)
    time_leave = models.TextField(null=True, blank=True)
    
    order = models.IntegerField(default=1)
    trip = models.ForeignKey("Trip", related_name="locs", on_delete=models.CASCADE)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('trversal:view-loc', args=[str(self.id)])

    

    
    # def delete(self, request, *args, **kwargs):
    #     self.day_pk = self.get_object().day.pk
    #     return super(LocDeleteView, self).delete(request, *args, **kwargs)