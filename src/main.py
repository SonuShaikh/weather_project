from src.api_client import WeatherApiClient
from src.constants import *
from src.database.db_connection import PostgresDB
import json
import datetime 


def insert_city_date(db, data):
    cursor = db.get_cursor()

    insert_query = """
        INSERT INTO city_info (city_name, country_code, state_name, latitude, longitude)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING;
    """

    for record in data:
        city_name = record.get("name")
        country_code = record.get("country")
        state_name = record.get("state", None)
        latitude = record.get("lat")
        longitude = record.get("lon")

        cursor.execute(insert_query, (city_name, country_code, state_name, latitude, longitude))

    db.conn.commit()
    cursor.close()
    print("City data inserted successfully!")

def main():
    try:

        #city = input("Enter the City name").strip()
        client = WeatherApiClient()
        data = client.get_weather("Mumbai")
        print(json.dumps(data, indent=4))


        for city in capital_cities:
            '''
            data = client.get_cityinfo(city)

            if data:
                print(f"response data {data}")

                # Update data to database
                db = PostgresDB()
                db.connect()
                insert_city_date(db, data)
                db.close()
            else:
                print("failed to fetch weather data")
            '''
    except Exception as e:
        print(f"exception {e}")



if __name__ == "__main__":
    main()