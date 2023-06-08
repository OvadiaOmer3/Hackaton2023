from sqlmodel import SQLModel, Enum
from typing import Optional




class TravelModeEnum(Enum):
    driving = "DRIVING"
    walking = "WALKING"
    bicycling = "BICYCLING"
    transit = "TRANSIT"


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

class RouteModel(SQLModel):
    # id: int = Field(default=None, primary_key=True)
    mode: TravelModeEnum
    distance: int
    duration: int
    origin: str
    destination: str
    fare: Optional[int] = None
    walking_duration: Optional[int] = None
    
    walking_distance: Optional[int] = None
    bus_distance: Optional[int] = None
    car_distance: Optional[int] = None
    train_distance: Optional[int] = None
    cycling_distance: Optional[int] = None
    
    # Not yet implemented
    taxi_distance: Optional[int] = None
    e_scooter_distance: Optional[int] = None


    departure_time: Optional[int] = None
    arrival_time: Optional[int] = None
