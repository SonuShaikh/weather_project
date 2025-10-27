import os
from dotenv import load_dotenv

load_dotenv()  # read from .env file

API_BASE_URL = os.getenv("API_BASE_URL")
API_KEY = os.getenv("API_KEY")


# Read environment variables
DB_NAME     = os.getenv("DB_NAME")
DB_USER     = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST     = os.getenv("DB_HOST")
DB_PORT     = os.getenv("DB_PORT")