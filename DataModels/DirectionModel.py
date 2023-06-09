from pydantic import BaseModel
from DataModels.RouteModel import RouteResponse

class DirectionRequest(BaseModel):
    user_id: int
    origin: str
    destination: str

class DirectionResponse(BaseModel):
    user_id: int
    request: DirectionRequest
    routes: list[RouteResponse]