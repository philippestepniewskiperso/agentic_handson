import httpx
from pydantic_extra_types.coordinate import Longitude, Latitude

from travel.domain.agent import agent
from travel.domain.models import Location


@agent.tool_plain
def location_tool(city_name: str) -> Location:
    with httpx.Client() as client:
        r = client.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": city_name, "count": 1}
        )
        result = r.json()["results"][0]
        return Location(latitude=Latitude(result["latitude"]), longitude=Longitude(result["longitude"]))


if __name__ == "__main__":
    print(location_tool("Paris"))