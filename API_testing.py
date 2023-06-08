import requests
import json

# Function to retrieve route information from Google Maps API
def get_route_info(mode, origin, destination):
    # Replace "YOUR_API_KEY" with your actual Google Maps API key
    api_key = "AIzaSyDd31MWU4GtAcjtm7aBWoptT7TRkkCXNdw"

    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&mode={mode}&key={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)

    return(data)

get_route_info(mode= "bicycling",origin= "tel+aviv+rabin+square", destination= "bugrashov+beach+tel+aviv")