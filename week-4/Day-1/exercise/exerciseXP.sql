CREATE TABLE customers (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR (50),
	last_name VARCHAR (50)
);


INSERT INTO customers (first_name , last_name)
VALUES('greg','jones'),
('sandra','jones')

SELECT * FROM items,customers
SELECT * FROM items WHERE price > 80
SELECT * FROM items WHERE price <= 300
SELECT * FROM customers WHERE last_name = 'smith' -- no operator matches the given name  and arguments types. you might need to add explicit type casts
SELECT * FROM customers WHERE last_name = 'jones'
SELECT * FROM customers WHERE first_name != 'scott'
