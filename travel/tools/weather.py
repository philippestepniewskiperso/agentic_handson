import logging

import openmeteo_requests
from datetime import datetime, timedelta, UTC

from pydantic_extra_types.coordinate import Longitude, Latitude

from travel.domain.agent import agent
from travel.domain.models import Weather, Location


@agent.tool_plain
def weather_tool(
        location: Location, start_date: str, end_date: str
) -> list[Weather]:
    """
    This tools allows to retrieve weather data for a given location and a given start and end date.
    All parameters are mandatory
    :param location: Location for which the weather data should be retrieved. It contains the latitude and longitude of the location.
    :param start_date: Start date for the forecast for retrieving weather data.
    :param end_date: End date for the forecast for retrieving weather data.
    :return:
    """
    openmeteo = openmeteo_requests.Client()
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": location.latitude,
        "longitude": location.longitude,
        "daily": ["temperature_2m_max", "precipitation_sum", "sunshine_duration"],
        "start_date": start_date,
        "end_date": end_date,
    }
    print("Fetching weather data" + str(params))
    responses = openmeteo.weather_api(url, params=params)
    daily = responses[0].Daily()

    temps = daily.Variables(0).ValuesAsNumpy().tolist()
    precips = daily.Variables(1).ValuesAsNumpy().tolist()
    sunshines = daily.Variables(2).ValuesAsNumpy().tolist()

    start = datetime.fromtimestamp(daily.Time(), UTC)
    interval = timedelta(seconds=daily.Interval())
    dates = [(start + i * interval).strftime("%Y-%m-%d") for i in range(len(temps))]

    return [
        Weather(date=date, temperature=temp, precipitation=precip, sunshine=sunshine)
        for date, temp, precip, sunshine in zip(dates, temps, precips, sunshines)
    ]


if __name__ == "__main__":
    paris_gps = Location(latitude=Latitude(48.85341), longitude=Longitude(2.3488))
    print(weather_tool(paris_gps, "2026-05-02", "2026-05-04"))
