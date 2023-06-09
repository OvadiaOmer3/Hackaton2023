from Utilities.GoogleDirection.DirectionAPI import DirectionAPI
from Utilities.DB.DB_mock import DB
from Utilities.GoogleDirection.RouteFilter import filter_routes
from Route_aggregation import presentable_data
from DataModels.UserModel import User


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


def main(origin: str, destination: str, user_id: int):
    db = DB()
    user = db.get_user(user_id)
    routes_list = DirectionAPI().get_directions(origin, destination)

    routes_list = filter_routes(routes_list)

    for i, r in enumerate(routes_list):
        # routes_list[0] should be the car route
        tmp_response = presentable_data(r, routes_list[0], user)
        r.response = tmp_response
        print(f"Route {i}: {tmp_response}")


    print(f"Routes Count: {len(routes_list)}")

    # Now the user have all the routes data and he can choose the route he wants to take
    chosen_route = routes_list[int(input("Enter chosen route index: "))]

    # Now we need to update the user data
    user.current_score = chosen_route.response.score
    user.tokens += chosen_route.response.tokens
    user.trips_count += 1

    user.rank = rank_calculator(user)


# if __name__ == "__main__":
#     origin = "Haifa"
#     destination = "Ashdod"
#     current_user_id = 2
#     main(origin, destination, current_user_id)

if __name__ == "__main__":
    origin = input("Enter origin: ")
    destination = input("Enter destination: ")
    current_user_id = int(input("Enter user id: "))
    main(origin, destination, current_user_id)
