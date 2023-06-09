from pydantic import BaseModel
from datetime import datetime as DateTime
from typing import Optional
from enum import Enum


class TravelModeEnum(Enum):
    driving = "driving"
    walking = "walking"
    bicycling = "bicycling"
    transit = "transit"


class TransitModeEnum(Enum):
    bus = "BUS"
    cable_car = "CABLE_CAR"
    commuter_train = "COMMUTER_TRAIN"
    ferry = "FERRY"
    funicular = "FUNICULAR"
    gondola_lift = "GONDOLA_LIFT"
    heavy_rail = "HEAVY_RAIL"
    high_speed_train = "HIGH_SPEED_TRAIN"
    intercity_bus = "INTERCITY_BUS"
    long_distance_train = "LONG_DISTANCE_TRAIN"
    metro_rail = "METRO_RAIL"
    monorail = "MONORAIL"
    other = "OTHER"
    rail = "RAIL"
    share_taxi = "SHARE_TAXI"
    subway = "SUBWAY"
    tram = "TRAM"
    trolleybusa = "TROLLEYBUS"


class RouteResponse(BaseModel):
    mode: TravelModeEnum
    arrival_time: Optional[DateTime] = None
    total_time: Optional[DateTime] = None
    walking_duration: Optional[int] = None
    
    walking_distance: Optional[int] = None
    fare: Optional[int] = None
    tokens: Optional[int] = None
    health_benefit: Optional[int] = None
    co2_emissions: Optional[float] = None
    eco_relative_to_car: Optional[int] = None
    score: Optional[float] = None


class RouteModel(BaseModel):
    # id: int = Field(default=None, primary_key=True)
    mode: TravelModeEnum
    distance: int
    duration: int
    origin: str
    destination: str
    fare: Optional[int] = None
    walking_duration: Optional[int] = None
    
    walking_distance: Optional[int] = 0
    bus_distance: Optional[int] = 0
    car_distance: Optional[int] = 0
    train_distance: Optional[int] = 0
    cycling_distance: Optional[int] = 0
    
    # Not yet implemented not found in google maps api
    taxi_distance: Optional[int] = 0
    e_scooter_distance: Optional[int] = 0


    departure_time: Optional[DateTime] = None
    arrival_time: Optional[DateTime] = None
    

    response: Optional[RouteResponse] = None

