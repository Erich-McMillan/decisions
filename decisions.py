
import googlemaps
import json
import random

# initialize maps object
gmaps = googlemaps.Client(key='AIzaSyDotSlWY4l-6M6-faeBFAzYBZEkg_zFLeo')

# query user for their address
userlocation = input('what is your current address? : ')

# convert user location to a lat/lng location
geocode_result = gmaps.geocode(userlocation)
# print(type(geocode_result[0]))
geocode_result_dict = geocode_result[0]
# print(type(geocode_result_dict['geometry']))
# print(geocode_result_dict['geometry']['location'])

userlatlng = [geocode_result_dict['geometry']['location']['lat'], geocode_result_dict['geometry']['location']['lng']]
print(userlatlng)

# get restaurants nearby
placenearby_result = gmaps.places_nearby(location=userlatlng,radius=1000,type='restaurant')
print(type(placenearby_result['results']))
placenearby_result_list = placenearby_result['results']

# print a list of places found
for i in range(0,len(placenearby_result_list)):
	print(i)
	print(placenearby_result_list[i]['name'])
	print('-------------')

# get user to input a list of restaurants from the list
indices_of_okay = input('list the numbers of the restaurants you want to select from separated by , : ')
okay = [int(s) for s in indices_of_okay.split(',')]
output = []

for i in range(0,len(okay)):
	output.append(placenearby_result_list[okay[i]]['name'])

print("Your result will be randomly selected from the following:")
print(output)

# seed the generator and select a random restaurant from the list
random.seed()
# result = placenearby_result_list[random.randrange(len(placenearby_result_list))]['name']
result = output[random.randrange(len(output))]
print("The final result is:")
print(result)
