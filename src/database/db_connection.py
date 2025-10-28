# src/database/db_connection.py

import psycopg2
from psycopg2 import OperationalError
from config.settings import *
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

class PostgresDB:
    def __init__(self):
        self.conn = None

    def connect(self):
        """Establish a PostgreSQL database connection."""
        try:
            self.conn = psycopg2.connect(
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT
            )
            logger.info("Database connection successful!")
            return self.conn
        except OperationalError as e:
            logger.info("Database connection failed: {e}")
            raise

    def get_cursor(self):
        """Return a cursor object for executing SQL queries."""
        if not self.conn:
            self.connect()
        return self.conn.cursor()

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            self.conn = None
            logger.info("Database connection closed.")