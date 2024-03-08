#!/usr/bin/env python
# coding: utf-8
Q1. What is a database? Differentiate between SQL and NoSQL databases.---> A database is a structured collection of data that is organized and stored in a way that allows for efficient retrieval, management, and manipulation of data.
SQL Databases:

SQL databases are based on the relational data model.

They use a tabular structure consisting of rows and columns, where data is organized into tables.

They enforce a predefined schema, meaning that the structure of the data is determined in advance.

SQL databases support ACID (Atomicity, Consistency, Isolation, Durability) properties, which ensure data integrity and transactional consistency.

SQL databases use structured query language (SQL) for defining and manipulating the data.

Examples of popular SQL databases include MySQL, PostgreSQL, Oracle Database, and Microsoft SQL Server.

NoSQL Databases:

NoSQL databases use various data models other than the traditional relational model.

They are designed to handle large amounts of unstructured or semi-structured data, such as JSON, XML, or key-value pairs.

NoSQL databases provide flexible schemas, allowing for dynamic and scalable data structures.

They are highly scalable and capable of handling high-velocity and high-volume data.

NoSQL databases typically sacrifice some ACID properties in favor of performance and scalability.

NoSQL databases use different query languages or APIs based on their data model. Examples include MongoDB (document-oriented), Cassandra (wide column), and Redis (key-value).Q2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.DDL stands for Data Definition Language. It is a subset of SQL (Structured Query Language) used to define and manage the structure of a database.
CREATE: This statement is used to create a new database object. For example, to create a table named "Customers" with columns for "ID," "Name," and "Email," you can use the following SQL statement:
# CREATE TABLE Customers (
#     ID INT PRIMARY KEY,
#     Name VARCHAR(50),
#     Email VARCHAR(100)
# );
DROP: The DROP statement is used to delete an existing database object
# DROP TABLE Customers;
ALTER: ALTER statement is used to modify the structure of an existing database object
# ALTER TABLE Customers
# ADD Phone VARCHAR(20);
TRUNCATE: TRUNCATE is used to delete all the data in a table, but it keeps the table structure intact.
# TRUNCATE TABLE Customers;
Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.DML stands for Data Manipulation Language. It is a subset of SQL (Structured Query Language) used to manipulate and interact with the data stored in a database.INSERT: The INSERT statement is used to insert new records into a table. You specify the table name and provide the values for the columns you want to populate.
# INSERT INTO Employees (ID, Name, Salary)
# VALUES (1, 'John Doe', 50000);
UPDATE: The UPDATE statement is used to modify existing records in a table
# UPDATE Employees
# SET Salary = 55000
# WHERE ID = 1;
# 
DELETE: The DELETE statement is used to remove records from a table.
# DELETE FROM Employees
# WHERE Salary < 50000;
Q4. What is DQL? Explain SELECT with an example.
DQL stands for Data Query Language. It is a subset of SQL (Structured Query Language) used to retrieve and query data from a database.

# SELECT ID, Name
# FROM Customers;
This statement retrieves the ID and Name columns from the "Customers" table and displays them as the result. You can also apply conditions using the WHERE clause to filter the dataQ5. Explain Primary Key and Foreign Key.Primary Key:
A primary key is a column or a set of columns in a database table that uniquely identifies each row or record in that table

Uniqueness: Each value in the primary key column(s) must be unique within the table.

Non-nullability: The primary key column(s) cannot contain null values.

Stability: The value of the primary key should not change for a given row once it is assigned.Foreign Key:
A foreign key is a column or a set of columns in a database table that refers to the primary key of another table.Referential Integrity: The foreign key establishes a relationship between tables, ensuring that data integrity is maintained across related tables.

Referenced Table: The foreign key references the primary key of another table, called the referenced table.

Relationship: The foreign key represents a relationship between the referencing table (where the foreign key is defined) and the referenced table.Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method.
# import mysql.connector
# 
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="abc",
#   password="password"
# )
# print(mydb)
# mycursor = mydb.cursor("select * from test.test_table")
# for i in mycursor.fetchall() :
#     print(i)
# mydb.close()
Q7. Give the order of execution of SQL clauses in an SQL query.The general order of execution for SQL clauses in a query is as follows:

FROM: Specifies the table or tables from which to retrieve data.

JOIN: Performs any necessary joins between tables, combining data from multiple tables based on specified conditions.

WHERE: Filters the data based on specified conditions, restricting the result set.

GROUP BY: Groups the data based on specified columns.

HAVING: Filters the grouped data based on specified conditions.

SELECT: Specifies the columns to be retrieved from the result set.

DISTINCT: Removes duplicate rows from the result set.

ORDER BY: Sorts the result set based on specified columns.

LIMIT/OFFSET: Limits the number of rows returned by the query or specifies a starting point for retrieving rows.
# In[ ]:





# In[ ]:




