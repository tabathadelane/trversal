import urllib.request, json
from . import secrets

from .models import Day, Location
# UniqueConstraint in meta class in model to tell django that you can only have days and orders so that day order pairs can be unique


def make_location_list(day):
    locations = day.location_set
    # list_len = len(locations)
    location_list = [l.name for l in locations]
    print(location_list)
    return location_list


# def get_route_time(origin, destination):
def get_route_time():
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    api_key = secrets.api_key

    # origin = origin.replace(' ','+')
    # destination = destination.replace(' ','+')
    origin = "portland, or".replace(' ','+')
    destination = "medford, or".replace(' ','+')

    nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
    request = endpoint + nav_request
    response = urllib.request.urlopen(request).read()
    directions = json.loads(response)

    time=directions['routes'][0]['legs'][0]['duration']['text']
    seconds = directions['routes'][0]['legs'][0]['duration']['value']

    print(time, seconds)
    return time