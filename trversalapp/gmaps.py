import urllib.request, json
import datetime as dt
import requests
import time
from . import secrets

from .models import Trip, Location
def time_gen(trip):
    format = "%I:%M %p"
    locations = trip.locs.all()
    location_list = [l.g_name for l in locations]
    if locations:
      clock = dt.datetime.strptime(str(locations[0].trip.start_time), '%H:%M:%S')
      locations[0].route_time = 0
      locations[0].save()

      for l in range(len(locations)-1):
        o_lat = locations[l].g_lat
        o_lng = locations[l].g_lng
        d_lat = locations[l+1].g_lat
        d_lng = locations[l+1].g_lng
        mode = locations[l].trip.mode
        route = gmaps_time(o_lat, o_lng, d_lat, d_lng, mode)
        locations[l+1].route_time = route
        locations[l+1].save()

      for l in range (len(locations)):
        arrive = clock + dt.timedelta(seconds=locations[l].route_time)
        leave = arrive + dt.timedelta(hours =int(locations[l].duration_hour), minutes = int(locations[l].duration_min))
        locations[l].time_arr = arrive.strftime(format)
        locations[l].time_leave = leave.strftime(format)
        locations[l].save()
        clock = leave
      return location_list
    else: 
      pass

def gmaps_time(o_lat, o_lng, d_lat, d_lng, mode):
    # GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/directions/json?'
    GOOGLE_MAPS_API_URL = f'https://maps.googleapis.com/maps/api/directions/json?origin={o_lat},{o_lng}&destination={d_lat},{d_lng}&mode=walking&key={secrets.api_key}'

    req = requests.get(GOOGLE_MAPS_API_URL)
    response = req.json()

    seconds = response['routes'][0]['legs'][0]['duration']['value']

    return seconds

# def date_setter(day):
#   # format = "%a %B, %d"
#   # format = "%Y-%m-%d"
#   date = dt.datetime.strptime(str(day.trip_name.start_day), "%Y-%m-%d")
#   change = day.day_order - 1
#   date = date + dt.timedelta(days=change)
#   day.day_date = date
#   day.save()

def geocode(trip):
  locations = trip.locs.all()
  if locations:
    for i in range (len(locations)):
      GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

      params = {
          'address' : locations[i].g_name,
          'key': secrets.api_key
      }

      req = requests.get(GOOGLE_MAPS_API_URL, params=params)
      response = req.json()
      locations[i].g_lat = response['results'][0]['geometry']['location']['lat']
      locations[i].g_lng = response['results'][0]['geometry']['location']['lng']
      locations[i].save()

def reorder_locs(trip):
  counter = 1
  for loc in trip.locs.all():
    loc.order = counter
    counter+=1
    loc.save()
    
# def reorder_days(trip):
#   counter = 1
#   for day in trip.days.all():
#     date_setter(day)
#     day.day_order = counter    
#     counter+=1
#     day.save()


