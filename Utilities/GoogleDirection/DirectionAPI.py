
# Write Mockup for Google Direction API

import googlemaps as gmaps
from DataModels.RouteModel import RouteModel, TravelModeEnum


class DirectionAPI:
    def __init__(self):
        self.api_key = "AIzaSyC-9dWUWb1C4QK5DZqjvE3zLx8XwTQr9qQ"
        self.gmaps = gmaps.Client(key=self.api_key)

    def get_directions(self, origin, destination):
        directions = []
        for mode in TravelModeEnum:
            directions_result = self.gmaps.directions(origin, 
                                                      destination,
                                                      mode=mode.value)
            RouteModel(
                mode=mode,
                distance=directions_result[0]['legs'][0]['distance']['value'],
                duration=directions_result[0]['legs'][0]['duration']['value'],
                origin=origin,
                destination=destination,
                fare=directions_result[0].get('fare')['value'],
                walking_distance=self.sum_distance_by_mode(directions_result, TravelModeEnum.walking),
                walking_duration=self.sum_duration_by_mode(directions_result, TravelModeEnum.walking),

            )

    def sum_distance_by_mode(self, directions, mode):
        total_distance = 0
        for step in directions[0]['legs'][0]['steps']:
            if step['travel_mode'] == mode:
                total_distance += step['distance']['value']
        return sum(directions['distance'])
    
    def sum_duration_by_mode(self, directions, mode):
        total_duration = 0
        for step in directions[0]['legs'][0]['steps']:
            if step['travel_mode'] == mode:
                total_duration += step['duration']['value']
        return sum(directions['duration'])

