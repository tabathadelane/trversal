from django.db import models

class Trip(models.Model):
    trip_name = models.CharField(max_length=100)
    days_num = models.IntegerField(default=1)
    start_day = models.DateField(default="2002-02-22")
    start_location = models.TextField(default="Portland, OR")
    creator = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.trip_name

class Day(models.Model):
    start_time = models.TimeField(default="9:00 AM")
    day_date = models.IntegerField(default=1)
    trip_name = models.ForeignKey("Trip", on_delete=models.CASCADE)

    def __str__(self):
        return (f'Day {self.day_date}')

class Location(models.Model):
    name = models.TextField(default=" ")
    duration_hour = models.IntegerField(default=1)
    duration_min = models.IntegerField(default=0)
    route_time = models.TextField(null=True, blank=True)
    order = models.IntegerField(default=1)
    day = models.ForeignKey("Day", on_delete=models.CASCADE)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name