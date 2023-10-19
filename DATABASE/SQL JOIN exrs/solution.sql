-- Task 1

SELECT student.name AS "Student",
	   mentor.name AS "Mentor",
	   student.city AS "Student's City",
	   mentor.city AS "Mentor's City"
FROM mentor
JOIN student
ON mentor.id = student.mentor_id
ORDER BY student.name;


-- Task 2 

SELECT student.name AS "Student",
	   mentor.name AS "Mentor",
	   student.city AS "Student's City",
	   mentor.city AS "Mentor's City"
	   
FROM mentor
FULL OUTER JOIN student
ON mentor.id = student.mentor_id
ORDER BY student.name;	


-- Task 3
SELECT mentor.name AS "Mentor",
       student.name AS "Student",
	   mentor.city AS "Mentor's City",
	   student.city AS "Student's City" 	   
FROM mentor
FULL OUTER JOIN student
ON mentor.id = student.mentor_id
WHERE mentor.name IS NOT NULL
ORDER BY mentor.name;


-- Task 4
SELECT mentor.name AS "Mentor",
       student.name AS "Student",
	   mentor.city AS "Mentor's City",
	   student.city AS "Student's City" 	   
FROM mentor
LEFT JOIN student 
ON student.mentor_id = mentor.id
WHERE mentor.city = 'Berlin'
OR student.city = 'Berlin'
ORDER BY mentor.name;

-- Task 5

SELECT
  student.name AS student,
  mentor.city AS city,
  mentor.name AS mentor
FROM student
JOIN mentor 
ON student.city = mentor.city
ORDER BY mentor.city, student.name, mentor.name;

