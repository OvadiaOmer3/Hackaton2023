# Pseudo code for route aggregation
# Takes the route data from RouteModel and aggregates to user presentable data

def token_calculator(route_object, user_rank):
    tokens = 0

    if route_object.mode == "car":
        tokens = 1
    elif route_object.mode == "taxi":
        tokens = 2
    else:
        # finish later!!!!

    return(tokens)


def health_benefit_calculator(route_object): # This function will calculate calories burned by walking and cycling
    health_benefit = 0

    if route_object.walk_distance != 0 or route_object.cycling_distance != 0:
        walking_distance_km = route_object.walking_distance/1000
        cycling_distance_km = route_object.cycling_distance/1000
        health_benefit = walking_distance_km * 42 + cycling_distance_km * 30
    else:
        health_benefit = 0

    return(health_benefit)

def co2_emissions_calculator(route_object): # This function will calculate co2 emissions for the route
    co2_emissions = 0

    return(co2_emissions)

def rank_change_calculator(route_object): # This function will calculate rank change for the route
    rank_change = 0

    return(rank_change)


def presentable_data(route_object):
    mode = route_object.mode
    arrival_time = route_object.arrival_time
    total_time = route_object.duration
    walking_distance = route_object.walking_distance
    walking_duration = route_object.walking_duration
    cost = route_object.fare
    tokens = token_calculator(route_object, user_rank)   # This will be a function that calculates tokens reward for the route
    health_benefit = health_benefit_calculator(route_object)   # This will be a function that calculates health benefit for the route
    co2_emissions = co2_emissions_calculator(route_object)   # This will be a function that calculates co2 emissions for the route
    rank_change = rank_change_calculator(route_object)   # This will be a function that calculates rank change for the 

    out_dict = {"mode": mode , "arrival_time": arrival_time, "total_time": total_time, "walking_distance": walking_distance, 
                "walking_duration": walking_duration, "cost": cost, "tokens": tokens, "health_benefit": health_benefit, 
                "co2_emissions": co2_emissions, "rank_change": rank_change}
    
    return(out_dict)