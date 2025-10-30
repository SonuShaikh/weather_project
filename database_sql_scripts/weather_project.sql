-- weather project

-- CREATE TABLE TO STORE CITY CO-ORDINATES
CREATE TABLE IF NOT EXISTS city_info (
    id SERIAL PRIMARY KEY,
    city_name VARCHAR(100),
    country_code VARCHAR(10),
    state_name VARCHAR(100),
    latitude FLOAT,
    longitude FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store weather data from API
CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    city_name VARCHAR(100) NOT NULL,
    country_code VARCHAR(10),
    temperature FLOAT,
    feels_like FLOAT,
    temp_min FLOAT,
    temp_max FLOAT,
    pressure INT,
    humidity INT,
    sea_level INT,
    grnd_level INT,
    visibility INT,
    recorded_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW(),
    raw_data JSONB              
);

CREATE INDEX indx_weather_city ON weather_data(city_name);

--drop table city_info



-- Create user
--CREATE USER python_user WITH PASSWORD 'secure_password';

-- Create database for the user
--CREATE DATABASE python_db OWNER python_user;

-- Optional: grant privileges on public schema (if using existing DB)
--GRANT ALL PRIVILEGES ON DATABASE python_db TO python_user;
