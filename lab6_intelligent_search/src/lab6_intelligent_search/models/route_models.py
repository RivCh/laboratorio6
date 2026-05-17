from pydantic import BaseModel

class RouteRequest(BaseModel):
    start: str
    goal: str

class BayesianRequest(BaseModel):
    has_fever: bool