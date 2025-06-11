Advanced MySQL Project

This project explores advanced features of MySQL to build a robust, efficient, and intelligent database. The focus is on moving beyond basic SELECT queries to implement data constraints, performance optimizations, and automated database logic.
Concepts Covered

This project contains a series of SQL scripts that demonstrate mastery of the following concepts:

    Tables with Constraints: Creating tables with rules like PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, and DEFAULT to ensure data integrity.
    Database Indexing: Using indexes to optimize query performance by speeding up data retrieval on frequently searched columns.
    Stored Procedures: Creating reusable SQL code blocks to perform complex, repetitive actions with input parameters.
    Stored Functions: Building functions that take input and return a single value, useful for encapsulating complex calculations.
    Database Views: Creating virtual tables to simplify complex queries and enhance security by restricting data access.
    Database Triggers: Automating actions (INSERT, UPDATE, DELETE) before or after data modification events on a table.

Requirements

    All scripts are designed to be executed on Ubuntu 20.04 LTS with MySQL 8.0.
    All SQL keywords are in UPPERCASE.
    Each SQL file begins with a comment describing its purpose.

How to Execute

To run any of the .sql files, you can use the cat command and pipe it into the mysql client:
Bash

$ cat <file_name.sql> | mysql -uroot -p <database_name>

For example, to execute a script named 0-create_users.sql on a database named my_db:
Bash

$ cat 0-create_users.sql | mysql -uroot -p my_db
Enter password:
