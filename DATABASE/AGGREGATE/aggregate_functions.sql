create database population ;
\c population
-- Create a table for city population data
CREATE TABLE city_population (
    city_id serial PRIMARY KEY,
    city_name VARCHAR(50),
    country_name VARCHAR(50),
    population INT,
    year INT
);

-- Insert 20 sample rows of population data
INSERT INTO city_population (city_name, country_name, population, year) VALUES
    ('New York City', 'United States', 8537673, 2020),
    ('Los Angeles', 'United States', 39776830, 2020),
    ('Chicago', 'United States', 2693976, 2020),
    ('Toronto', 'Canada', 2731571, 2020),
    ('London', 'United Kingdom', 8961989, 2020),
    ('Paris', 'France', 2148271, 2020),
    ('Sydney', 'Australia', 5312163, 2020),
    ('Mumbai', 'India', 12442373, 2020),
    ('Shanghai', 'China', 27382955, 2020),
    ('São Paulo', 'Brazil', 22043028, 2020),
    ('New York City', 'United States', 8419600, 2010),
    ('Los Angeles', 'United States', 37954200, 2010),
    ('Chicago', 'United States', 2695598, 2010),
    ('Toronto', 'Canada', 2503281, 2010),
    ('London', 'United Kingdom', 8173941, 2010),
    ('Paris', 'France', 2110694, 2010),
    ('Sydney', 'Australia', 4299195, 2010),
    ('Mumbai', 'India', 12478277, 2010),
    ('Shanghai', 'China', 23019148, 2010),
    ('São Paulo', 'Brazil', 19989307, 2010);


SELECT * 
FROM city_population 
ORDER BY country_name ;

-- city_id |   city_name   |  country_name  | population | year
---------+---------------+----------------+------------+------
--      17 | Sydney        | Australia      |    4299195 | 2010
--       7 | Sydney        | Australia      |    5312163 | 2020
--      10 | São Paulo     | Brazil         |   22043028 | 2020
--      20 | São Paulo     | Brazil         |   19989307 | 2010
--       4 | Toronto       | Canada         |    2731571 | 2020
--      14 | Toronto       | Canada         |    2503281 | 2010
--      19 | Shanghai      | China          |   23019148 | 2010
--       9 | Shanghai      | China          |   27382955 | 2020
--       6 | Paris         | France         |    2148271 | 2020
--      16 | Paris         | France         |    2110694 | 2010
--       8 | Mumbai        | India          |   12442373 | 2020
--      18 | Mumbai        | India          |   12478277 | 2010
--       5 | London        | United Kingdom |    8961989 | 2020
--      15 | London        | United Kingdom |    8173941 | 2010
--      11 | New York City | United States  |    8419600 | 2010
--       2 | Los Angeles   | United States  |   39776830 | 2020
--       3 | Chicago       | United States  |    2693976 | 2020
--       1 | New York City | United States  |    8537673 | 2020
--      12 | Los Angeles   | United States  |   37954200 | 2010
--      13 | Chicago       | United States  |    2695598 | 2010
--(20 rows)



SELECT country_name, AVG(population) as average_population 
FROM city_population 
GROUP BY country_name;

--  country_name  |  average_population
----------------+-----------------------
-- France         |  2129482.500000000000
-- United States  | 16679646.166666666667
-- China          | 25201051.500000000000
-- Australia      |  4805679.000000000000
-- United Kingdom |  8567965.000000000000
-- Canada         |  2617426.000000000000
-- India          | 12460325.000000000000
-- Brazil         | 21016167.500000000000
--(8 rows)


SELECT country_name, ROUND(AVG(population)) as average_population 
FROM city_population 
GROUP BY country_name;

--  country_name  | average_population
----------------+--------------------
-- France         |            2129483
-- United States  |           16679646
-- China          |           25201052
-- Australia      |            4805679
-- United Kingdom |            8567965
-- Canada         |            2617426
-- India          |           12460325
-- Brazil         |           21016168
--(8 rows)


SELECT year, ROUND(AVG(population)) as average_population 
FROM city_population 
GROUP BY year;

-- year | average_population
------+--------------------
-- 2020 |           13203083
-- 2010 |           12164324
--(2 rows)

SELECT country_name, SUM(population) AS total_population
FROM city_population
GROUP BY country_name;

--  country_name  | total_population
----------------+------------------
-- France         |          4258965
-- United States  |        100077877
-- China          |         50402103
-- Australia      |          9611358
-- United Kingdom |         17135930
-- Canada         |          5234852
-- India          |         24920650
-- Brazil         |         42032335
--(8 rows)


SELECT year,SUM(population) AS total_population
FROM city_population
GROUP BY year;

-- year | total_population
------+------------------
-- 2020 |        132030829
-- 2010 |        121643241
--(2 rows)


SELECT country_name,COUNT(city_id) AS city_count
FROM  city_population 
GROUP BY country_name;

--  country_name  | city_count
----------------+------------
-- France         |          2
-- United States  |          6
-- China          |          2
-- Australia      |          2
-- United Kingdom |          2
-- Canada         |          2
-- India          |          2
-- Brazil         |          2
--(8 rows)


SELECT year,COUNT(city_id) AS city_count
FROM city_population GROUP BY year;

-- year | city_count
------+------------
-- 2020 |         10
-- 2010 |         10
--(2 rows)


SELECT country_name,MIN(population) AS min_population
FROM city_population 
GROUP BY country_name;

--  country_name  | min_population
----------------+----------------
-- France         |        2110694
-- United States  |        2693976
-- China          |       23019148
-- Australia      |        4299195
-- United Kingdom |        8173941
-- Canada         |        2503281
-- India          |       12442373
-- Brazil         |       19989307
--(8 rows)


SELECT country_name,MIN(population) AS min_population_2020
FROM city_population
WHERE year = 2020 GROUP BY country_name;

--  country_name  | min_population_2020
----------------+---------------------
-- Australia      |             5312163
-- Brazil         |            22043028
-- Canada         |             2731571
-- China          |            27382955
-- France         |             2148271
-- India          |            12442373
-- United Kingdom |             8961989
-- United States  |             2693976
--(8 rows)


SELECT country_name,MAX(population) AS max_population
FROM city_population 
GROUP BY country_name;


SELECT country_name,MAX(population) AS max_population_2020
FROM city_population
WHERE year = 2020 GROUP BY country_name;


SELECT year,MAX(population) AS max_population
FROM city_population
GROUP BY year;








