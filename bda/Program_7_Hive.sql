--Use HIVE to create, alter, and drop databases, tables, views, functions and indexes

CREATE DATABASE employee_db;
USE employee_db;

ALTER DATABASE employee_db SET DBPROPERTIES ('Owner'='Admin');
DROP DATABASE employee_db CASCADE;

CREATE TABLE employees (
    emp_id INT,
    name STRING,
    age INT,
    dept_id INT,
    salary FLOAT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

LOAD DATA INPATH '/user/cloudera/employees.txt' INTO TABLE employees;

ALTER TABLE employees ADD COLUMNS (email STRING);
ALTER TABLE employees RENAME TO employees_new;
DROP TABLE employees_new;

CREATE VIEW high_salary_employees AS
SELECT emp_id, name, salary FROM employees WHERE salary > 50000;

ALTER VIEW high_salary_employees AS
SELECT emp_id, name, age, salary FROM employees WHERE salary > 60000;

DROP VIEW high_salary_employees;

ADD JAR /user/cloudera/custom_udf.jar;
CREATE FUNCTION to_upper AS 'com.example.hiveudf.ToUpperUDF';
SELECT to_upper(name) FROM employees;
DROP FUNCTION to_upper;

CREATE INDEX emp_dept_idx ON TABLE employees (dept_id)
AS 'org.apache.hadoop.hive.ql.index.compact.CompactIndexHandler'
WITH DEFERRED REBUILD;

ALTER INDEX emp_dept_idx ON employees REBUILD;
DROP INDEX emp_dept_idx ON employees;

SHOW TABLES;
DESCRIBE employees;
SELECT * FROM employees LIMIT 5;
