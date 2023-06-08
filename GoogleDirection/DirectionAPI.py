
# Write Mockup for Google Direction API

import json
import requests
import urllib.parse


class DirectionAPI:
    def __init__(self):
        self.api_key = "AIzaSyC-9dWUWb1C4QK5DZqjvE3zLx8XwTQr9qQ"

    def get_direction(self, origin, destination):
        
