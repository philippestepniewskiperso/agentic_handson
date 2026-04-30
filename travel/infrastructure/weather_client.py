import openmeteo_requests
from datetime import datetime, timedelta, UTC

from travel.domain.models import Weather


def fetch_weather(
    latitude: float, longitude: float, start_date: str, end_date: str
) -> list[Weather]:
    openmeteo = openmeteo_requests.Client()
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": ["temperature_2m_max", "precipitation_sum", "sunshine_duration"],
        "start_date": start_date,
        "end_date": end_date,
    }
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
