# class recreated to insert data into database

from src.database.db_connection import PostgresDB
import json


class DatabaseOperations:
    def __init__(self):
        self.db = PostgresDB()
        self.db.connect()

    def insert_weather_data(self,data):
        try:
            cursor = self.db.get_cursor()
            columns = data.keys()
            values = [json.dumps(v) if isinstance(v, dict) else v for v in data.values()]
            insert_query = f"""
                    INSERT INTO weather_data ({','.join(columns)})
                    VALUES ({', '.join(['%s']* len(columns))})
            """
            cursor.execute(insert_query,values)
            print('Weather data inserted successfully')

            self.db.conn.commit()
            cursor.close()
        except Exception as e:
            print(f"Insert Error: {e}")
        
    def insert_city_data(self, data):
        try:
            cursor = self.db.get_cursor()

            insert_query = """
                INSERT INTO city_info (city_name, country_code, state_name, latitude, longitude)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT DO NOTHING;
            """
            # fetch records
            for record in data:
                city_info = data.get('name')
                country_name = data.get('country')
                state_name = data.get('state')
                latitude = data.get('lat')
                longitude = data.get('lon')

                # insert record
                cursor.execute(insert_query,(city_info,country_name,state_name,latitude,longitude))

            self.db.conn.commit()
            cursor.close()
            print(f"{city_info} data inserted successfully!")
        except BaseException as e:
            print(f"Database Operation error {e}")