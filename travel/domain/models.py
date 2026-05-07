from pydantic import BaseModel, Field
from pydantic_extra_types.coordinate import Longitude, Latitude
from datetime import date as Date


class Weather(BaseModel):
    date: str = Field(description="Date of weather forecast")
    temperature: float = Field(description="Temperature forecasted")
    precipitation: float = Field(description="Precipitation forecasted")
    sunshine: float = Field(description="Sunshine forecasted")


class DayPlan(BaseModel):
    date: Date = Field(description="Date of day for the plan ")
    city: str = Field(description="City name for the plan")
    weather: Weather = Field(description="Weather forecasted for the date")
    activities: list[str] = Field(description="List of activities for the plan")


class TravelPlan(BaseModel):
    destination: str = Field(description="Destination of the travel plan")
    start_date: Date = Field(description="Start date of travel plan")
    end_date: Date = Field(description="End date of travel plan")
    days: list[DayPlan] = Field(description="List of day plans per day between start_date and end_date")
    budget_estimate: str = Field(description="Budget estimate for travel plan for all days")


class Location(BaseModel):
    latitude: Latitude
    longitude: Longitude


class TravelResponse(BaseModel):
    response:str = Field(description="A nice response presenting the travel plan in a human-friendly way")