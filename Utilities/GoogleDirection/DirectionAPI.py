
# Write Mockup for Google Direction API

import googlemaps as gmaps
from DataModels.RouteModel import RouteModel, TravelModeEnum, TransitModeEnum


class DirectionAPI:
    def __init__(self):
        self.api_key = "AIzaSyDd31MWU4GtAcjtm7aBWoptT7TRkkCXNdw"
        self.gmaps = gmaps.Client(key=self.api_key)

    def get_directions(self, origin, destination) -> list[RouteModel]:
        routes_list = []

        for mode in TravelModeEnum:
            directions_result = self.gmaps.directions(origin, 
                                                      destination,
                                                      mode=mode.value)
            
            total_train_distance = self.sum_distance_by_mode(directions_result, TravelModeEnum.transit, [TransitModeEnum.commuter_train.value,
                                                                                                         TransitModeEnum.heavy_rail.value,
                                                                                                         TransitModeEnum.high_speed_train.value,
                                                                                                         TransitModeEnum.long_distance_train.value, 
                                                                                                         TransitModeEnum.metro_rail.value, 
                                                                                                         TransitModeEnum.monorail.value, 
                                                                                                         TransitModeEnum.rail.value, 
                                                                                                         TransitModeEnum.subway.value, 
                                                                                                         TransitModeEnum.tram.value])            

            routes_list.append(RouteModel(
                mode=mode,
                distance=directions_result[0]['legs'][0]['distance']['value'],
                duration=directions_result[0]['legs'][0]['duration']['value'],
                origin=origin,
                destination=destination,
                fare=directions_result[0].get('fare')['value'] if directions_result[0].get('fare') else None,
                car_distance=self.sum_distance_by_mode(directions_result, TravelModeEnum.driving.value),
                cycling_distance=self.sum_distance_by_mode(directions_result, TravelModeEnum.bicycling.value),
                walking_distance=self.sum_distance_by_mode(directions_result, TravelModeEnum.walking.value),
                bus_distance=self.sum_distance_by_mode(directions_result, TravelModeEnum.transit.value, TransitModeEnum.bus.value),
                train_distance=total_train_distance,
                walking_duration=self.sum_duration_by_mode(directions_result, TravelModeEnum.walking.value),

            ))
        
        return routes_list


    def sum_distance_by_mode(self, directions, mode, sub_modes=[]):
        total_distance = 0
        for step in directions[0]['legs'][0]['steps']:
            if step['travel_mode'].lower() == mode:
                if sub_modes != []:
                    if step['transit_details']['line']['vehicle']['type'] in sub_modes:
                        total_distance += step['distance']['value']
                else:
                    total_distance += step['distance']['value']
        return total_distance
    
    def sum_duration_by_mode(self, directions, mode):
        total_duration = 0
        for step in directions[0]['legs'][0]['steps']:
            if step['travel_mode'] == mode:
                total_duration += step['duration']['value']
        return total_duration

