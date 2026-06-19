import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='YOUR_API_KEY_HERE')

now = datetime.now()
start_point = input("Enter start location:")
destination = input("Enter destination:")
directions_result = gmaps.directions(
    start_point,
    destination,
    mode="transit",
    departure_time=now
)

for step in directions_result[0]['legs'][0]['steps']:
    if step['travel_mode'] == 'TRANSIT':
        bus_data = step['transit_details']
        bus_num = bus_data['line']['short_name']
        departure_stop = bus_data['departure_stop']['name']
        departure_time = bus_data['departure_time']['text']
        
        print(f"Bus/Train {bus_num} leaves from {departure_stop} at {departure_time}")