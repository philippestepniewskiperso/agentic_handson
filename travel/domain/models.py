from pydantic import BaseModel
from pydantic_extra_types.coordinate import Longitude, Latitude
from datetime import date


class Weather(BaseModel):
    date: str
    temperature: float
    precipitation: float
    sunshine: float


class DayPlan(BaseModel):
    date: date
    city: str
    weather: Weather
    activities: list[str]


class TravelPlan(BaseModel):
    destination: str
    start_date: date
    end_date: date
    days: list[DayPlan]
    budget_estimate: str


class Location(BaseModel):
    latitude: Latitude
    longitude: Longitude
