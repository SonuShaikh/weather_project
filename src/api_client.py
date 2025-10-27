import requests
from config.settings import API_BASE_URL, API_KEY

class WeatherApiClient:
    def __init__(self):
        self.base_url = API_BASE_URL
        self.api_key = API_KEY

    # Fetch city weather details
    def get_weather(self, city):
        url = f"{self.base_url}/geo/1.0/direct?"
        param = {"q":city,"appid":self.api_key}
        try:
            response = requests.get(url,param,timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API error {e}")
            return None
            