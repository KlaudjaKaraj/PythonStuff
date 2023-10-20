-- Create a table to store information about train schedules
CREATE TABLE train_schedule (
    schedule_id serial PRIMARY KEY,
    train_name varchar(50) NOT NULL,
    departure_station varchar(50) NOT NULL,
    arrival_station varchar(50) NOT NULL,
    departure_time timestamp NOT NULL,
    duration interval,
    available_seats integer,
    ticket_price numeric(8, 2)
);


-- Insert sample data for 10 rows
INSERT INTO train_schedule (train_name, departure_station, arrival_station, departure_time, duration, available_seats, ticket_price)
VALUES
    ('Express 101', 'City A', 'City B', '2023-10-18 08:00:00', '2 hours 30 minutes', 100, 50.00),
    ('Local 202', 'City B', 'City C', '2023-10-18 09:30:00', '2 hours 45 minutes', 150, 30.00),
    ('Fast Train 303', 'City X', 'City Y', '2023-10-18 10:00:00', '1 hour 45 minutes', 120, 60.00),
    ('Commuter 404', 'City Y', 'City Z', '2023-10-18 12:15:00', '1 hour 30 minutes', 80, 25.00),
    ('Metro 505', 'City P', 'City Q', '2023-10-18 14:30:00', '45 minutes', 200, 10.00),
    ('Express 606', 'City B', 'City D', '2023-10-18 15:30:00', '3 hours', 70, 75.00),
    ('Local 707', 'City D', 'City E', '2023-10-18 16:45:00', '2 hours 15 minutes', 90, 35.00),
    ('Shuttle 808', 'City R', 'City S', '2023-10-18 18:00:00', '30 minutes', 50, 5.00),
    ('Rapid 909', 'City M', 'City N', '2023-10-18 19:00:00', '1 hour 30 minutes', 110, 45.00),
    ('Express 1010', 'City E', 'City F', '2023-10-18 20:30:00', '1 hour', 60, 20.00);



-- Query the train schedule and calculate arrival_time
SELECT
    schedule_id,
    train_name,
    departure_station,
    arrival_station,
    departure_time,
    duration,
    departure_time + duration AS arrival_time,
    available_seats,
    ticket_price
FROM train_schedule;

--schedule_id |   train_name   | departure_station | arrival_station |   departure_time    | duration |    arrival_time     | available_seats | ticket_price
-------------+----------------+-------------------+-----------------+---------------------+----------+---------------------+-----------------+--------------
--           1 | Express 101    | City A            | City B          | 2023-10-18 08:00:00 | 02:30:00 | 2023-10-18 10:30:00 |             100 |        50.00
--           2 | Local 202      | City B            | City C          | 2023-10-18 09:30:00 | 02:45:00 | 2023-10-18 12:15:00 |             150 |        30.00
--           3 | Fast Train 303 | City X            | City Y          | 2023-10-18 10:00:00 | 01:45:00 | 2023-10-18 11:45:00 |             120 |        60.00
--           4 | Commuter 404   | City Y            | City Z          | 2023-10-18 12:15:00 | 01:30:00 | 2023-10-18 13:45:00 |              80 |        25.00
--           5 | Metro 505      | City P            | City Q          | 2023-10-18 14:30:00 | 00:45:00 | 2023-10-18 15:15:00 |             200 |        10.00
--           6 | Express 606    | City B            | City D          | 2023-10-18 15:30:00 | 03:00:00 | 2023-10-18 18:30:00 |              70 |        75.00
--           7 | Local 707      | City D            | City E          | 2023-10-18 16:45:00 | 02:15:00 | 2023-10-18 19:00:00 |              90 |        35.00
--           8 | Shuttle 808    | City R            | City S          | 2023-10-18 18:00:00 | 00:30:00 | 2023-10-18 18:30:00 |              50 |         5.00
--           9 | Rapid 909      | City M            | City N          | 2023-10-18 19:00:00 | 01:30:00 | 2023-10-18 20:30:00 |             110 |        45.00
--          10 | Express 1010   | City E            | City F          | 2023-10-18 20:30:00 | 01:00:00 | 2023-10-18 21:30:00 |              60 |        20.00
--(10 rows)


SELECT
    schedule_id,
    train_name,
    departure_station,
    arrival_station,
    departure_time,
    duration,
    departure_time + duration AS arrival_time,
    available_seats,
    ticket_price
FROM train_schedule
WHERE duration < '2 hours';


-- schedule_id |   train_name   | departure_station | arrival_station |   departure_time    | duration |    arrival_time     | available_seats | ticket_price
-------------+----------------+-------------------+-----------------+---------------------+----------+---------------------+-----------------+--------------
--           3 | Fast Train 303 | City X            | City Y          | 2023-10-18 10:00:00 | 01:45:00 | 2023-10-18 11:45:00 |             120 |        60.00
--           4 | Commuter 404   | City Y            | City Z          | 2023-10-18 12:15:00 | 01:30:00 | 2023-10-18 13:45:00 |              80 |        25.00
--           5 | Metro 505      | City P            | City Q          | 2023-10-18 14:30:00 | 00:45:00 | 2023-10-18 15:15:00 |             200 |        10.00
--           8 | Shuttle 808    | City R            | City S          | 2023-10-18 18:00:00 | 00:30:00 | 2023-10-18 18:30:00 |              50 |         5.00
--           9 | Rapid 909      | City M            | City N          | 2023-10-18 19:00:00 | 01:30:00 | 2023-10-18 20:30:00 |             110 |        45.00
--          10 | Express 1010   | City E            | City F          | 2023-10-18 20:30:00 | 01:00:00 | 2023-10-18 21:30:00 |              60 |        20.00
--(6 rows)

SELECT
    schedule_id,
    train_name,
    departure_station,
    arrival_station,
    departure_time,
    duration,
    departure_time + duration AS arrival_time,
    available_seats,
    ticket_price
FROM train_schedule
WHERE departure_time BETWEEN '2023-10-18 08:00:00' AND '2023-10-18 10:00:00';


--schedule_id |   train_name   | departure_station | arrival_station |   departure_time    | duration |    arrival_time     | available_seats | ticket_price
-------------+----------------+-------------------+-----------------+---------------------+----------+---------------------+-----------------+--------------
--           1 | Express 101    | City A            | City B          | 2023-10-18 08:00:00 | 02:30:00 | 2023-10-18 10:30:00 |             100 |        50.00
--           2 | Local 202      | City B            | City C          | 2023-10-18 09:30:00 | 02:45:00 | 2023-10-18 12:15:00 |             150 |        30.00
--           3 | Fast Train 303 | City X            | City Y          | 2023-10-18 10:00:00 | 01:45:00 | 2023-10-18 11:45:00 |             120 |        60.00
--(3 rows)



SELECT NOW();



SELECT CURRENT_TIME;