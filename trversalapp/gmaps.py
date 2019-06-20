import urllib.request, json
import datetime as dt
import time
from . import secrets

from .models import Trip, Day, Location
# look into UniqueConstraint in meta class in model to tell django that you can only have days and orders so that day order pairs can be unique

# thistrip = Trip.objects.get(pk=1)
# day = thistrip.days.get(pk=1)
def time_gen(day):
    format = "%I:%M %p"
    locations = day.locs.all()
    location_list = [l.g_name for l in locations]
    if locations:
      # hour = int(locations[0].day.start_time_hour)
      # minute = int(locations[0].day.start_time_min)
      clock = dt.datetime.strptime(str(locations[0].day.start_time), '%H:%M:%S')
      # clock = dt.datetime(2019, 1, 1, hour = hour, minute = minute) #9:00:00
      locations[0].route_time = 0
      locations[0].save()

      for l in range(len(locations)-1):
        # print(locations[l].duration_hour)
        origin = locations[l].g_name
        destination = locations[l+1].g_name
        route = gmaps_time(origin, destination)
        locations[l+1].route_time = route
        locations[l+1].save()

      for l in range (len(locations)):
        arrive = clock + dt.timedelta(seconds=locations[l].route_time)
        leave = arrive + dt.timedelta(hours =int(locations[l].duration_hour), minutes = int(locations[l].duration_min))
        # print(arrive.strftime(format), leave.strftime(format))
        locations[l].time_arr = arrive.strftime(format)
        locations[l].time_leave = leave.strftime(format)
        locations[l].save()
        clock = leave
        # print(clock.strftime(format))
      return location_list
    else: 
      pass

def gmaps_time(origin, destination):
# def get_route_time():
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    api_key = secrets.api_key

    origin = origin.replace(' ','+')
    destination = destination.replace(' ','+')
    # origin = "portland, or".replace(' ','+')
    # destination = "medford, or".replace(' ','+')

    nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
    request = endpoint + nav_request
    response = urllib.request.urlopen(request).read()
    directions = json.loads(response)

    # time=directions['routes'][0]['legs'][0]['duration']['text']
    seconds = directions['routes'][0]['legs'][0]['duration']['value']

    # print(time)
    return seconds

# time_gen(day)
def date_setter(day):
  # format = "%a %B, %d"
  # format = "%Y-%m-%d"
  date = dt.datetime.strptime(str(day.trip_name.start_day), "%Y-%m-%d")
  change = day.day_order - 1
  date = date + dt.timedelta(days=change)
  # day.day_date = date.strftime(format)
  day.day_date = date
  day.save()