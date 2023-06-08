# Example code from chatgpt

import requests
import json

# Function to retrieve route information from Google Maps API
def get_route_info(mode):
    # Replace "YOUR_API_KEY" with your actual Google Maps API key
    api_key = "YOUR_API_KEY"
    origin = "Point A"  # Replace with the starting point
    destination = "Point B"  # Replace with the destination

    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&mode={mode}&key={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)

    if data["status"] == "OK":
        route = data["routes"][0]
        duration = route["legs"][0]["duration"]["text"]
        distance = route["legs"][0]["distance"]["text"]
        # Additional information like cost can be retrieved from other APIs if available
        cost = 0  # Replace with actual cost retrieval logic
        return duration, cost, distance
    else:
        return None, None, None

# Available modes of transportation
modes = ["driving", "taxi", "transit", "bicycling", "walking"]

# Data table to store route information
data_table = []

# Retrieve route information for each mode and populate the data table
for mode in modes:
    duration, cost, distance = get_route_info(mode)
    data_table.append({"Mode": mode.capitalize(), "Time": duration, "Cost": cost, "Length": distance})

# Print the data table
print("Route Information:")
print("-------------------")
print("Mode\t\tTime\t\tCost\t\tLength")
print("------------------------------------------")
for data in data_table:
    print(f"{data['Mode']}\t{data['Time']}\t{data['Cost']}\t{data['Length']}")
