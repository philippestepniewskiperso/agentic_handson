from pydantic import BaseModel


class TravelRequest(BaseModel):
    pass


class TravelAdvice(BaseModel):
    pass


class Weather(BaseModel):
    date: str
    temperature: float
    precipitation: float
    sunshine: float
