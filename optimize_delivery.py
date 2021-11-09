import googlemaps
import json
from datetime import datetime

with open("api_key.txt") as f:
    api_key = f.read()
gmaps = googlemaps.Client(key=api_key)

customers = ["220 Marvin Ln, Piscataway, NJ 08854",
"New Gibbons Residence Campus, Gibbons Residence Hall B - House A5-A6, New Gibbons Residence Campus, New Brunswick, NJ 08901",
"1450 Redmond St, North Brunswick Township, NJ 08902"]

restaurant = ["49 Bayard St, New Brunswick, NJ 08901",
"252 Plainfield Ave, Edison, NJ 08817",
"1045 Easton Ave #1625, Somerset, NJ 08873"]

deliverers = [(40.50488500478356, -74.4670101053852),
(40.523748244622425, -74.47182690442412),
(40.501203991220244, -74.41227952116414)]

curr_c = customers[0]
curr_r = restaurant[0]

min_time = float("inf")
best_d = -1
to_c = gmaps.directions(curr_r, curr_c, mode="driving")
total_time = to_c[0]["legs"][0]["duration"]["value"]
for i, d in enumerate(deliverers):
    to_r = gmaps.directions(d, curr_r, mode="driving")
    d_time = to_r[0]["legs"][0]["duration"]["value"]
    if d_time < min_time:
        min_time = d_time
        deliverers = i

total_time = total_time + min_time
print(total_time)

