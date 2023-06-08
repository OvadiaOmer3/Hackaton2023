# Pseudo code for route aggregation
# Takes the route data from RouteModel and aggregates to user presentable data

def presentable_data(route_object):
    arrival_time = route_object.arrival_time
    total_time = route_object.duration
    walking_distance = route_object.walking_distance
    walking_duration = route_object.walking_duration
    cost = route_object.fare
    tokens = token_calculator(route_object, user_rank)   # This will be a function that calculates tokens reward for the route
    health_benefit = health_benefit_calculator(route_object)   # This will be a function that calculates health benefit for the route
    co2_emissions = co2_emissions_calculator(route_object)   # This will be a function that calculates co2 emissions for the route
    rank_change = rank_change_calculator(route_object)   # This will be a function that calculates rank change for the 

    out_dict = {"arrival_time": arrival_time, "total_time": total_time, "walking_distance": walking_distance, 
                "walking_duration": walking_duration, "cost": cost, "tokens": tokens, "health_benefit": health_benefit, 
                "co2_emissions": co2_emissions, "rank_change": rank_change}
    
    return(out_dict)