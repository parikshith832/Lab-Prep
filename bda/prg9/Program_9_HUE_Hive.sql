CREATE DATABASE IF NOT EXISTS company;
USE company;

CREATE TABLE employees (
    id INT,
    name STRING,
    department STRING,
    salary INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

LOAD DATA INPATH '/user/cloudera/data/employees.csv'
INTO TABLE employees;

SELECT * FROM employees;

SELECT department, MAX(salary) AS highest_salary
FROM employees
GROUP BY department;

SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department;
/*
Generate Reports in HUE 
Step 1: Export Query Results 
1. Run any of the above SQL queries in HUE Query Editor 
2. Click Export → Choose format (CSV, Excel, JSON) 
3. Download the report 
Step 2: Create HUE Dashboard for Visualization 
1. Open HUE → Click Dashboard 
2. Click Create New Dashboard 
3. Click Add Widget → Select Chart Type (Bar Chart, Pie Chart, etc.) Enter Query → 
Example for Employee Count
*/