import psycopg2
from config.settings import *

# connectivity function
def db_connection():

    try:
        conn = psycopg2.connect(
            dbname      =  DB_NAME,
            user        =  DB_USER,
            password    =  DB_PASSWORD,
            host        =  DB_HOST,
            port        =  DB_PORT

        )
        print('Database connection successfull!')
    except Exception as e:
        print (f'Database connection failed {e}')


if __name__ == "__main__":
    db_connection()
