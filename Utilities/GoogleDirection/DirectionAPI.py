
# Write Mockup for Google Direction API

import googlemaps as gmaps
from DataModels.RouteModel import RouteModel, TravelModeEnum, TransitModeEnum


class DirectionAPI:
    def __init__(self):
        self.api_key = "AIzaSyC-9dWUWb1C4QK5DZqjvE3zLx8XwTQr9qQ"
        self.gmaps = gmaps.Client(key=self.api_key)

    def get_directions(self, origin, destination):
        routes_list = []
        for mode in TravelModeEnum:
            directions_result = self.gmaps.directions(origin, 
                                                      destination,
                                                      mode=mode.value)
            
            total_train_distance = self.sum_distance_by_mode(directions_result, TravelModeEnum.transit, [TransitModeEnum.commuter_train,
                                                                                                         TransitModeEnum.heavy_rail,
                                                                                                         TransitModeEnum.high_speed_train,
                                                                                                         TransitModeEnum.long_distance_train, 
                                                                                                         TransitModeEnum.metro_rail, 
                                                                                                         TransitModeEnum.monorail, 
                                                                                                         TransitModeEnum.rail, 
                                                                                                         TransitModeEnum.subway, 
                                                                                                         TransitModeEnum.tram])
            

            routes_list.append(RouteModel(
                mode=mode,
                distance=directions_result[0]['legs'][0]['distance']['value'],
                duration=directions_result[0]['legs'][0]['duration']['value'],
                origin=origin,
                destination=destination,
                fare=directions_result[0].get('fare')['value'],
                car_distance=self.sum_distance_by_mode(directions_result, TravelModeEnum.driving),
                cycling_distance=self.sum_distance_by_mode(directions_result, TravelModeEnum.bicycling),
                walking_distance=self.sum_distance_by_mode(directions_result, TravelModeEnum.walking),
                bus_distance=self.sum_distance_by_mode(directions_result, TravelModeEnum.transit, TransitModeEnum.bus),
                train_distance=total_train_distance,
                walking_duration=self.sum_duration_by_mode(directions_result, TravelModeEnum.walking),

            ))
        
        return routes_list

        

    def sum_distance_by_mode(self, directions, mode, sub_modes=[]):
        total_distance = 0
        for step in directions[0]['legs'][0]['steps']:
            if step['travel_mode'] == mode:
                if sub_modes is not []:
                    if step['transit_details']['line']['vehicle']['type'] in sub_modes:
                        total_distance += step['distance']['value']
                else:
                    total_distance += step['distance']['value']
        return sum(directions['distance'])
    
    def sum_duration_by_mode(self, directions, mode):
        total_duration = 0
        for step in directions[0]['legs'][0]['steps']:
            if step['travel_mode'] == mode:
                total_duration += step['duration']['value']
        return sum(directions['duration'])

