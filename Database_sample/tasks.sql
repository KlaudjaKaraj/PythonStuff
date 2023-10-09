-- Task 1
INSERT INTO public.musicians (first_name, last_name, date_of_birth, instrument) VALUES
('Justin', 'Bieber', '1994-03-01 00:00:00', 'Voice'),
('Lady', 'Gaga', '1986-03-28 00:00:00', 'Voice'),
('Alejandro', 'Sanz', '1968-12-18 00:00:00', 'Voice'),
('Jimmy', 'Hendrix', '1942-11-27 00:00:00', 'Guitar'),
('Charlie', 'Parker', '1920-08-29 00:00:00', 'Saxophone');


-- Task 2
SELECT * FROM public.musicians


-- Task 3
SELECT * FROM public.musicians ORDER BY date_of_birth;

SELECT * FROM public.musicians ORDER BY date_of_birth desc;


-- Task 4
DELETE FROM public.musicians 
WHERE first_name IN ('Justin' , 'Lady', 'Alejandro', 'Jimmy', 'Charlie');

SELECT * FROM public.musicians ORDER BY date_of_birth desc;


-- Task 5
UPDATE public.musicians SET instrument = 'Saxophone' 
WHERE instrument = 'Saxphone';


-- Task 6
UPDATE public.musicians SET instrument = 'Piano' 
WHERE first_name = 'Bernhard' and last_name = 'Schwarzenegger';

SELECT instrument FROM public.musicians 
WHERE first_name = 'Bernhard' and last_name = 'Schwarzenegger';


-- Task 7
SELECT last_name, date_of_birth FROM public.musicians 
WHERE first_name = 'Araceli' and instrument = 'Piano';


-- Task 8
SELECT first_name, last_name, instrument FROM public.musicians 
WHERE instrument IN ('Piano', 'Guitar') 
ORDER BY instrument, last_name ;


-- Task 9
SELECT * FROM public.musicians 
WHERE first_name = 'Araceli' and instrument IN ('Piano', 'Guitar')
ORDER BY date_of_birth desc
LIMIT 3;


-- Task 10
SELECT DISTINCT instrument FROM public.musicians 
ORDER BY instrument;


-- Task 11
SELECT first_name AS Name, 
    last_name AS 'Family Name', 
    date_of_birth AS 'Date of birth'
FROM public.musicians
WHERE instrument = 'Harp' AND last_name LIKE 'M%'
ORDER BY date_of_birth asc
OFFSET 3
LIMIT 1;


-- Task 12
SELECT * FROM public.musicians
WHERE NOT last_name LIKE 'Y%' 
    AND NOT last_name LIKE 'M%' 
    AND NOT last_name LIKE 'C%' 
    AND NOT last_name LIKE 'A%'
ORDER BY last_name ASC,first_name ASC
OFFSET 5
LIMIT 5;


-- Task 13
SELECT * FROM public.musicians
WHERE instrument IN ('Guitar', 'Saxophone', 'Cello', 'Violin', 'Harp')


-- Task 14
TRUNCATE TABLE public.musicians;

SELECT * FROM public.musicians;

