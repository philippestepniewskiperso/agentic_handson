import httpx
from pydantic_extra_types.coordinate import Longitude, Latitude

from travel.domain.models import Location


def location_tool(city_name: str) -> Location:
    """
    Tool to retrieve city coordinates
    :param city_name: City name in string
    :return: Location object with latitude and longitude
    """
    print("Running tool 'location_tool'")
    with httpx.Client() as client:
        r = client.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": city_name, "count": 1}
        )
        result = r.json()["results"][0]
        return Location(latitude=Latitude(result["latitude"]), longitude=Longitude(result["longitude"]))


if __name__ == "__main__":
    print(location_tool("Paris"))