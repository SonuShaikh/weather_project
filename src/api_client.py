import requests
import logging
import datetime
from config.settings import API_BASE_URL, API_KEY


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

class WeatherApiClient:
    def __init__(self):
        self.base_url = API_BASE_URL
        self.api_key = API_KEY
        self.timeout = 10  # seconds

    # Fetch city coardinates
    def get_cityinfo(self, city):
        url = f"{self.base_url}/geo/1.0/direct"
        params = {
            "q": city,
            "appid": self.api_key
        }

        try:
            logger.info(f"Fetching weather data for city: {city}")
            response = requests.get(url, params=params, timeout=self.timeout)

            # Check HTTP status code
            if response.status_code == 200:
                logger.info(f"Data fetched successfully for {city}")
                return self.clean_response(response.json())
            elif response.status_code == 401:
                logger.error("Unauthorized: Check your API key")
            elif response.status_code == 404:
                logger.warning(f"City {city} not found")
            else:
                logger.error(f"Unexpected status code: {response.status_code}")
            return None

        except requests.exceptions.Timeout:
            logger.error(f"Request timed out for city: {city}")
        except requests.exceptions.ConnectionError:
            logger.error("Network problem occurred")
        except requests.exceptions.RequestException as e:
            logger.error(f"API error occurred: {e}")
        
        return None
    
    # Fetch city weather data
    def get_weather(self, city):
        try:
            url = f"{API_BASE_URL}/data/2.5/weather?"
            params = {
                "q":city,
                "appid":API_KEY,
                "units":"metric"
            }
            response = requests.get(url,params=params,timeout=self.timeout)
            
            # Check HTTP status code
            if response.status_code == 200:
                logger.info(f"Data fetched successfully for {city}")
                return self.parse_weather_data(response.json())
            elif response.status_code == 401:
                logger.error("Unauthorized: Check your API key")
            elif response.status_code == 404:
                logger.warning(f"City {city} not found")
            else:
                logger.error(f"Unexpected status code: {response.status_code}")
            return None
            
        except requests.exceptions.ConnectTimeout as e:
            print(f"API Error: {e}")
        except requests.exceptions.ConnectionError as e:
            print(f"API Error: {e}")
        except requests.exceptions.RequestException as e:
            print(f"API Error: {e}")

    # Clean Json Response
    def clean_response(self, jsonResponse):
        cleaned_response = [
            {k:v for k,v in city.items() if k != 'local_names'}
            for city in jsonResponse 
        ]
        return cleaned_response
    
    # Extract relevant weather fields from API JSON.
    # Returns a dict ready for DB insertion.
    def parse_weather_data(self, data):
        return {
            "city_name": data.get("name"),
            "country_code": data.get("sys", {}).get("country"),
            "temperature": data.get("main", {}).get("temp"),
            "feels_like": data.get("main", {}).get("feels_like"),
            "temp_min": data.get("main", {}).get("temp_min"),
            "temp_max": data.get("main", {}).get("temp_max"),
            "pressure": data.get("main", {}).get("pressure"),
            "humidity": data.get("main", {}).get("humidity"),
            "sea_level": data.get("main", {}).get("sea_level"),
            "grnd_level": data.get("main", {}).get("grnd_level"),
            "visibility": data.get("visibility"),
            "recorded_at": datetime.datetime.fromtimestamp(data.get("dt")).isoformat(),
            "raw_data": data  
        }
