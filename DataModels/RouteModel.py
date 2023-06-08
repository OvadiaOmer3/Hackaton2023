from sqlmodel import SQLModel, Enum
from typing import Optional


class TravelModeEnum(Enum):
    driving = "DRIVING"
    walking = "WALKING"
    bicycling = "BICYCLING"
    transit = "TRANSIT"


class RouteModel(SQLModel):
    # id: int = Field(default=None, primary_key=True)
    mode: TravelModeEnum
    distance: int
    duration: int
    origin: str
    destination: str
    fare: Optional[int] = None
    walking_distance: Optional[int] = None
    walking_duration: Optional[int] = None
    cycling_distance: Optional[int] = None
    departure_time: Optional[int] = None
    arrival_time: Optional[int] = None
