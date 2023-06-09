from Utilities.GoogleDirection.DirectionAPI import DirectionAPI
from Utilities.DB.DB_mock import DB
from Utilities.GoogleDirection.RouteFilter import filter_routes
from Route_aggregation import presentable_data
from DataModels.UserModel import User
from DataModels.DirectionModel import DirectionRequest, DirectionResponse


def rank_calculator(user):
    rank = 1
    if user.current_score in range(10,30):
        rank = 2
    elif user.current_score in range(30,50):
        rank = 3
    elif user.current_score in range(50,80):
        rank = 4
    elif user.current_score in range(80,100):
        rank = 5

    return(rank)


def main(direction_request: DirectionRequest):
    db = DB()
    user = db.get_user(direction_request.user_id)
    routes_list = DirectionAPI().get_directions(direction_request.origin, direction_request.destination)

    routes_list = filter_routes(routes_list)

    response = DirectionResponse(user_id=direction_request.user_id,
                                 request=direction_request,
                                 routes=[])
    
    for i, r in enumerate(routes_list):
        # routes_list[0] should be the car route
        r.response = presentable_data(r, routes_list[0], user)
        response.routes.append(r.response)

    print(response.json(indent=4))    

    print(f"\nRoutes Count: {len(routes_list)}")

    # Now the user have all the routes data and he can choose the route he wants to take
    chosen_route = routes_list[int(input("Enter chosen route index: "))]

    # Now we need to update the user data
    user.current_score = chosen_route.response.score
    user.tokens += chosen_route.response.tokens
    user.trips_count += 1

    user.rank = rank_calculator(user)

    db.update_user(user=user)


# if __name__ == "__main__":
#     origin = "Tel Aviv University"
#     destination = "Rabin Square, Tel Aviv-Yafo"
#     current_user_id = 2
#     main(direction_request=DirectionRequest(user_id=current_user_id, origin=origin, destination=destination))

if __name__ == "__main__":
    origin = input("Enter origin: ")
    destination = input("Enter destination: ")
    current_user_id = int(input("Enter user id: "))
    main(direction_request=DirectionRequest(user_id=current_user_id, origin=origin, destination=destination))
