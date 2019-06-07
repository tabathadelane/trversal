import urllib.request, json
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = ''

origin = input('Where are you?: ').replace(' ','+')
destination = input('Where do you want to go?: ').replace(' ','+')

nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
request = endpoint + nav_request
response = urllib.request.urlopen(request).read()
directions = json.loads(response)

time=directions['routes'][0]['legs'][0]['duration']['text']
seconds = directions['routes'][0]['legs'][0]['duration']['value']

print(time, seconds)