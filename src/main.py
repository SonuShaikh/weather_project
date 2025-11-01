from src.api_client import WeatherApiClient
from src.database.db_connection import PostgresDB
from src.constants import capital_cities
from src.database.db_crud_operation import *
import json
import datetime 
import traceback


def main():
    try:
        #city = input("Enter the City name").strip()
        client = WeatherApiClient()
        crud_operation = DatabaseOperations()

        for city in capital_cities:

            data = client.get_weather(city)
            #print(json.dumps(data, indent=4))
            crud_operation.insert_weather_data(data)

    except Exception as e:
        print(f"exception {e}")
        traceback.print_exc()


if __name__ == "__main__":
    main()