def filter_routes(routes_list):
    routes = []
    distance_lst = []
    min_distance = 0
    duration_lst = []
    min_duration = 0

    for route in routes_list: #save all distance and duration to list
        distance_lst.append(route.distance)
        duration_lst.append(route.duration)
    
    min_distance = min(distance_lst) #find min distance
    min_duration = min(duration_lst) #find min duration

    for i, route in enumerate(routes_list):
        if i==0: #if first route (Drive) 
            routes.append(route) #add to routes list

        elif route.duration <= min_duration*2: #if duration is less than 2 times of min duration
            if route.distance <= min_distance*2: #if distance is less than 2 times of min distance
                routes.append(route) #add to routes list
                
    return routes
