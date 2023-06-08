from Utilities.GoogleDirection.DirectionAPI import DirectionAPI
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


origin = input("Enter origin: ")
destination = input("Enter destination: ")
current_user = input("Enter user: ")

routes_list = DirectionAPI().get_direction(origin, destination)

for r in routes_list:
    tmp_dict = presentable_data(r, current_user)
    r.presentable_data_dict = tmp_dict


# Now the user have all the routes data and he can choose the route he wants to take
chosen_route = input("Enter chosen route: ")

# Now we need to update the user data
current_user.current_score = chosen_route.presentable_data_dict["score"]
current_user.past_relative_scores.append(tmp_dict["eco_relative_to_car"])
current_user.tokens += chosen_route.presentable_data_dict["tokens"]
current_user.rank = rank_calculator(current_user)