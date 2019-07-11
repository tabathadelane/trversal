from django.contrib.auth.models import User
from trversalapp.models import Trip, Day, Location
from rest_framework import serializers



# class LocSerializer(serializers.HyperlinkedModelSerializer):
class LocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('pk', 'order', 'day', 'name', 'g_name', 'g_lat', 'g_lng', 'time_arr', 'time_leave', 'url'  )

class DaySerializer(serializers.ModelSerializer):
    locs = LocSerializer(many=True)
    class Meta:
        model = Day
        fields = ('pk', 'day_order', 'day_date', 'start_time', 'trip_name', 'mode', 'url', 'locs', )

class TripSerializer(serializers.ModelSerializer):
    days = DaySerializer(many=True)
    class Meta:
        model = Trip
        fields = ( 'name', 'start_day', 'url', 'days',)


