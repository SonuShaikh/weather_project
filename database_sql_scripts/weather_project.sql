-- weather project


CREATE TABLE IF NOT EXISTS city_info (
    id SERIAL PRIMARY KEY,
    city_name VARCHAR(100),
    country_code VARCHAR(10),
    state_name VARCHAR(100),
    latitude FLOAT,
    longitude FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


--drop table city_info



-- Create user
--CREATE USER python_user WITH PASSWORD 'secure_password';

-- Create database for the user
--CREATE DATABASE python_db OWNER python_user;

-- Optional: grant privileges on public schema (if using existing DB)
--GRANT ALL PRIVILEGES ON DATABASE python_db TO python_user;
