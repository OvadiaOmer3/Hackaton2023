from pydantic import BaseModel
from enum import Enum
from typing import Optional


class User(BaseModel):
    id_key: int
    username: str
    password: str

    fullname: str
    age: str

    rank: int
    current_score: float
    trips_count: int
    tokens: int
    total_completed_trips: int
