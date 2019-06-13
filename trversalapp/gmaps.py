import urllib.request, json
import datetime as dt
from . import secrets

from .models import Trip, Day, Location
# UniqueConstraint in meta class in model to tell django that you can only have days and orders so that day order pairs can be unique
thistrip = Trip.objects.get(pk=1)
day = thistrip.day_set.get(pk=1)
# # def time_gen(day):
#     locations = day.location_set.all()
#     location_list = [l.name for l in locations]
#     if locations:
#       for l in range(len(locations)-1):
#           print(locations[l].duration_hour)
#           origin = locations[l].name
#           destination = locations[l+1].name
#           route = gmaps_time(origin, destination)
#           print(route)
#           locations[l+1].route_time = route
#           locations[l+1].save()
#           print(locations[l+1].route_time)

#           #pull 0(l) and 1(l+1)

#           #0.name is origin, 1.name is destination

#           #route_time = calculate

#           #set 1.route time

#           #++ the l's
#           # add arr and leave timefields to model?
#       #for l in range (len(locations)-1):
      
#         #if l > 0:
          
#           #pull l

          
#       # print(location_list)
#       # print(locations)
#       return location_list
#     else: 
#       pass

#     '''how to display in model and view:
#         i have a duration(timedelta) and a route time(timedelta)
#         clock is model.starttime(time-obj)
#         for loop:
#         route time(timedelta) + clock(time-obj) -> time-arr(time-obj)
#         time-arr(time-obj) + stay(timedelta) -> time-leave(time-obj)
#         set clock as time-leave(time-obj)
#         add to i's


#         calculate all in seconds? or time delta?
#         ***to set timedelta  = dt.timedelta(days = 1, hours = 3, minutes = 42, seconds = 54)
#         used to convert to seconds?
#         timedelta.total_seconds()
#         set new time object
#         ***time(0, 0, 0, 0) h,m,s, ms
#         (t1.hour, t1.minute)

#         stay = time(HOUR, MIN, 0, 0 )

#         time-arr.hour, time-arr.minute
#         plus timedelta with seconds to next clock time

#         zero-padded - for display
#         "Staying for {:d}:{:02d}".format(stay.hour, stay.minute) 

#         use another drop down to set time? or look for a clock widget

#         '''




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

    time=directions['routes'][0]['legs'][0]['duration']['text']
    seconds = directions['routes'][0]['legs'][0]['duration']['value']

    print(time)
    return seconds

# time_gen(day)