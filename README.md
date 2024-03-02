# Hackaton2023
This is our hackathon 2023 project

The problem:
Underestimation of environmental impact of transporation options
Misconception about the inconvenience of public transportation
Lack of incentives for travel with a positive impact on the environment

The solution:
Creating travel routes that weigh environmental parameters
Reflection of different travel considerations (time, direct cost, hidden cost, environmental)
Rating method and providing incentives:
Incentives in the form of a unique currency supported by supporting businesses
User-based rating that reflects different incentive options based on the rating

What this code does?
1. In the "main" module there's currently a partial version of the Backend logic.
   - Mimicing the user's search for a route between two points
   - Running the core functions
   - Returning output already formatted for Fronted use. 
2. The Backend receives the user's request, comprised of user_id, origin and destination. 
   the following steps then accure:
   - Using Google maps API we get the relevant data for all possible routes between the origin and destination.
   - Interepting the suggested routes data to create our route_object class for each route.
   - Analysing route data to calculate relevant parameters we wish to reflect to the user, 
     such as: time, distance, cost, environmental impact, etc.
   - Returning the data to the user in a presentable format.
   - Letting the user choose the route he wishes to take
   - Updating relevant user data based on his choice such as: tokens, rank and hidden score which determins the user rank.

3. If you will try to run the "main" file you can perform a simulation of a user's search, make sure to choose a user id between 1-10.

e.g.: Origin: "Tel Aviv University", Destination: "Rabin Square, Tel Aviv", User_id: 2

The simulation is interactive and will ask you for input for each step.
