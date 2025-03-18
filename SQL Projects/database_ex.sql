
--Creating a Database
CREATE DATABASE my_database;
USE my_database;

--Creating a Table
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    position VARCHAR(50),
    salary DECIMAL(10,2)
);

--Inserting Data
INSERT INTO employees (name, position, salary)
VALUES ('Alice', 'Software Engineer', 85000.00);

--Retrieving Data
SELECT *
FROM employees;

SELECT name, position
FROM employees WHERE salary > 70000.00;

--Updating Data for Alice
UPDATE employees
SET salary 90000.00;
WHERE name = 'Alice';

--Deleting Data

DELETE 
FROM employees 
WHERE name = 'Alice';

--If you have departments table;

CREATE TABLE departments (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(50)
);

SELECT employees.name, employees.position, departments.dept_name
FROM employees
INNER JOIN departments ON employees.dept_id = departments.dept_id;



