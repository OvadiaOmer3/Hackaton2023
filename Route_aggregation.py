# Pseudo code for route aggregation
# Takes the route data from RouteModel and aggregates to user presentable data

def presentable_data(route_object):
    arrival_time = route_object.arrival_time
    total_time = route_object.duration
    walking_time = route_object.walking_distance
    cost = route_object.fare
    tokens = token_calculator(route_object, user_rank)   # This will be a function that calculates tokens reward for the route
    health_benefit = health_benefit_calculator(route_object)   # This will be a function that calculates health benefit for the route
    co2_emissions = co2_emissions_calculator(route_object)   # This will be a function that calculates co2 emissions for the route
    