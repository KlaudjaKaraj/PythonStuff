CREATE DATABASE weather_db ;

CREATE TABLE temperature_data (
    location text,
    temperature_readings numeric[][]
);


INSERT INTO temperature_data (location, temperature_readings) VALUES
    ('New York', ARRAY[[12.3, 15.7, 18.1], [14.2, 17.5, 20.0], [10.8, 13.2, 15.9]]),
    ('Los Angeles', ARRAY[[22.6, 26.3, 24.5], [23.8, 27.1, 25.2], [21.2, 25.7, 23.0]]);



SELECT *
FROM temperature_data;

--  location   |                 temperature_readings
-------------+------------------------------------------------------
-- New York    | {{12.3,15.7,18.1},{14.2,17.5,20.0},{10.8,13.2,15.9}}
-- Los Angeles | {{22.6,26.3,24.5},{23.8,27.1,25.2},{21.2,25.7,23.0}}
--(2 rows)



SELECT location, temperature_readings[1][2]
FROM temperature_data;

--- location   | temperature_readings
-------------+----------------------
-- New York    |                 15.7
-- Los Angeles |                 26.3
--(2 rows)



SELECT location, temperature_readings[1][1:]
FROM temperature_data;

--location   | temperature_readings
-------------+----------------------
-- New York    | {{12.3,15.7,18.1}}
-- Los Angeles | {{22.6,26.3,24.5}}
--(2 rows)



-- Same as above
SELECT location, temperature_readings[1:1]
FROM temperature_data;

-- location   | temperature_readings
-------------+----------------------
-- New York    | {{12.3,15.7,18.1}}
-- Los Angeles | {{22.6,26.3,24.5}}
--(2 rows)



SELECT location, temperature_readings[1:2]
FROM temperature_data;

-- location   |        temperature_readings
-------------+-------------------------------------
-- New York    | {{12.3,15.7,18.1},{14.2,17.5,20.0}}
-- Los Angeles | {{22.6,26.3,24.5},{23.8,27.1,25.2}}
--(2 rows)



SELECT location, AVG(temperature_readings[i][j]) AS avg_temperature
FROM temperature_data
CROSS JOIN generate_subscripts(temperature_readings, 1) i
CROSS JOIN generate_subscripts(temperature_readings, 2) j                     
GROUP BY location;

-- location   |   avg_temperature
-------------+---------------------
-- Los Angeles | 24.3777777777777778
-- New York    | 15.3000000000000000
--(2 rows)


UPDATE temperature_data
SET temperature_readings[2][2] = 28.0
WHERE location = 'Los Angeles';