# Pseudo code for route aggregation
# Takes the route data from RouteModel and aggregates to user presentable data

def token_calculator(route_object, user_rank):
    tokens = 0
    
    if route_object.mode == "car":
        tokens = 1*user_rank
    elif route_object.mode == "taxi":
        tokens = 2*user_rank
    else:
        walking_km = route_object.walking_distance/1000
        bus_km = route_object.bus_distance/1000
        train_km = route_object.train_distance/1000
        cycling_km = route_object.cycling_distance/1000
        e_scooter_km = route_object.e_scooter_distance/1000
        tmp_tokens = 6*(walking_km+cycling_km) + 5*e_scooter_km + 4*train_km + 3*bus_km
        tokens = tmp_tokens*user_rank

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

def co2_emissions_calculator(route_object): #This function calculates the CO2 emissions of a given route (various modes of transport)
    emissions = 0
    bus_distance = route_object.bus_distance
    train_distance = route_object.train_distance
    car_distance = route_object.car_distance
    taxi_distance = route_object.taxi_distance
    e_scooter_distance = route_object.e_scooter_distance
    emissions = (bus_distance * 30) + (train_distance * 60) + (car_distance * 200) + (taxi_distance * 180) + (e_scooter_distance * 100)
    emissions = emissions / 1000
    #Emissions are calculated in kg per km, need to validate these values

    return(emissions)

def eco_relative(route_object): #This function calculates the eco relative to car
    car_co2_emmissions = co2_emissions_calculator(routes_list[0]) # list indexing for the car route object
    eco_relative = (co2_emissions_calculator(route_object) / car_co2_emmissions)*100
    return round(eco_relative)

def rank_change_calculator(route_object): # This function will calculate rank change for the route
    rank_change = 0

    return(rank_change)


def presentable_data(route_object, user_rank):
    mode = route_object.mode
    arrival_time = route_object.arrival_time
    total_time = route_object.duration
    walking_distance = route_object.walking_distance
    walking_duration = route_object.walking_duration
    cost = route_object.fare
    tokens = token_calculator(route_object, user_rank)   # This will be a function that calculates tokens reward for the route
    health_benefit = health_benefit_calculator(route_object)   # This will be a function that calculates health benefit for the route
    co2_emissions = co2_emissions_calculator(route_object)   # This will be a function that calculates co2 emissions for the route
    eco_relative_to_car = eco_relative(route_object)
    rank_change = rank_change_calculator(route_object)   # This will be a function that calculates rank change for the 

    out_dict = {"mode": mode , "arrival_time": arrival_time, "total_time": total_time, "walking_distance": walking_distance, 
                "walking_duration": walking_duration, "cost": cost, "tokens": tokens, "health_benefit": health_benefit, 
                "co2_emissions": co2_emissions, "eco_relative_to_car": eco_relative_to_car , "rank_change": rank_change}
    
    return(out_dict)