-- CREATE TABLE students(
-- 	id SERIAL PRIMARY KEY,
-- 	first_name VARCHAR (50),
-- 	last_name VARCHAR (50),
-- 	birth_date DATE
-- );
-- INSERT INTO students (first_name, last_name, birth_date) 
-- VALUES
-- ('Marc', 'Benichou', '1998/11/02'),
-- ('Yoan', 'Cohen', '2010/12/03'),
-- ('Lea', 'Benichou', '1987/07/27'),
-- ('Amelia', 'Dux', '1996/04/07'),
-- ('David', 'Grez', '2003/06/04'),
-- ('Omer', 'Simpson', '1980/10/03')
-- INSERT INTO students (first_name, last_name, birth_date) 
-- VALUES
-- ('Anas','Rasmally','2005/07/26');
-- select * from students
-- select first_name , last_name from students

-- select first_name , last_name from students WHERE id = 2
-- select first_name , last_name from students where first_name = 'Marc' and last_name = 'Benichou'
-- select first_name , last_name from students where first_name = 'Marc' or last_name = 'Benichou'
-- select first_name , last_name from students where first_name ILIKE '%a%'
-- select first_name , last_name from students where first_name ILIKE 'a%'
-- select first_name , last_name from students where first_name ILIKE '%a'
-- select first_name , last_name from students where first_name ILIKE '%a_'
-- select first_name , last_name from students where id in (1,3)
-- select * from students where birth_date >= '2000/01/1'


