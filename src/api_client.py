import requests
import logging
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

    # Fetch city weather details
    def get_weather(self, city):
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
                return response.json()
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
