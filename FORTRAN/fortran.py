# pip install geopy
# import module
from geopy.geocoders import Nominatim
from geopy import distance
import sys
from openpyxl import Workbook, load_workbook
wb = Workbook()
ws = wb.active
ws.title = "Data"

print("Enter your name. \n")
name = input(sys.argv[0])

print("Enter your email id. \n")
emailid = input(sys.argv[0])

print("Enter your roll no. \n")
rollno = input(sys.argv[0])

# initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")

# place input
print("Enter your place name. \n")
Input_place1 = "raipur"
Input_place2 = input(sys.argv[0])

# Get location of the input strings
place1 = geolocator.geocode(Input_place1)
place2 = geolocator.geocode(Input_place2)

print(place1)
print(place2)

# Get latitude and longitude
Loc1_lat, Loc1_lon = (place1.latitude), (place1.longitude)
Loc2_lat, Loc2_lon = (place2.latitude), (place2.longitude)

location1 = (Loc1_lat, Loc1_lon)
location2 = (Loc2_lat, Loc2_lon)

#display the distance
print(distance.distance(location1, location2).km, "kms \n")

ws.append([name, rollno, Input_place2, distance.distance(location1, location2).km, emailid])

wb.save('FORTRAN.xlsx')