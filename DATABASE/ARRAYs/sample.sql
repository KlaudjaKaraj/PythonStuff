CREATE TABLE country_table (
	id SERIAL PRIMARY KEY,
	country_code VARCHAR (3),
	flag_color TEXT ARRAY
	-- flag_color TEXT [])
);


INSERT INTO country_table(country_code, flag_color)
VALUES 
('USA', ARRAY ['red', 'white', 'blue']),    -- United States Of America
('BRA', ARRAY ['green', 'yellow', 'blue']), -- Brazil
('DEU', ARRAY ['black', 'red', 'yellow']),  -- Germany
('IND', ARRAY ['orange', 'green', 'white']);-- India

-- GET ALL THE DATA
SELECT country_code, flag_color
FROM country_table;

-- GET THE FIRST COLOR
SELECT country_code, flag_color[1] --arrays start from index 1
FROM country_table

-- RETURN THE TOTAL NUMBER OF ELEMENTS IN THE ARRAY
SELECT country_code, CARDINALITY (flag_color)
FROM country_table;

-- EXPANDING THE ARRAY INTO A SET OF ROWS

SELECT country_code,
UNNEST (flag_color)
FROM country_table
WHERE country_code = 'USA';


-- SEARCHING WHETHER THERE IS A COUNTRY CODE WITH RED FLAG COLOR IN IT
SELECT country_code, flag_color
FROM country_table
WHERE 'red' = ANY (flag_color)

-- RETURNING THE POSITION OF THE COLOR 'RED' // including null
SELECT country_code, 
       array_position(flag_color, 'red')
FROM country_table;

-- -//- not including null
SELECT country_code,
	   array_position(flag_color, 'red')
FROM country_table
WHERE 'red' = ANY (flag_color);


-- contains ' @> '
SELECT country_code, flag_color
FROM country_table
WHERE flag_color @> '{"black"}' ;


-- [starting index : ending index]
SELECT country_code,
       flag_color [1:2]
FROM country_table;


SELECT country_code,
       flag_color [1:3]
FROM country_table;


SELECT country_code,
       flag_color [2:3]
FROM country_table;