from sqlmodel import SQLModel, Enum
from typing import Optional


class User(SQLModel):
    id_key: int
    username: str
    password: str

    fullname: str
    age: str

    rank: int
    current_score: float
    past_relavtive_scores: list
    tokens: int
    total_completed_trips: int
