from src.api_client import WeatherApiClient

def main():
    city = input("Enter the City name").strip()
    client = WeatherApiClient()
    data = client.get_weather(city)

    if data:
        print(f"Co-ordinates for {data}")
    else:
        print("failed to fetch weather data")

if __name__ == "__main__":
    main()