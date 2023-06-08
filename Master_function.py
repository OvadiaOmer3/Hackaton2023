from GoogleDirection.DirectionAPI import DirectionAPI
from Route_aggregation import presentable_data

def rank_calculator(user):


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
current_user.rank = 