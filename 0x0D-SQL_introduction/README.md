# 0x0D-SQL Introduction

## Project Overview

This project aims to introduce the basics of SQL (Structured Query Language) and its implementation using MySQL. Through this project, learners will get hands-on experience with the fundamental concepts of databases such as creating, accessing, manipulating, and querying databases.

## Learning Objectives

- Understand what a database is, and the differences between databases and tables.
- Learn how to create a database and tables using SQL.
- Explore how to insert, update, and delete data from a database.
- Get familiar with querying data from a database using `SELECT`.
- Introduction to SQL syntax and best practices.

## Requirements

- All files are executed on Ubuntu 20.04 LTS using `MySQL 8.0 (version 8.0.25)`.
- All files end with a new line.
- SQL queries should have a comment just before (i.e., syntax above).
- All SQL keywords should be in uppercase (`SELECT`, `WHERE`, etc.).
- A `README.md` file, at the root of the folder of the project, is mandatory.
- The length of files will be tested using `wc`.

## Files

| File Name                 | Description |
|---------------------------|-------------|
| `0-list_databases.sql`    | Script that lists all databases of your MySQL server. |
| `1-create_database_if_missing.sql` | Script to create a database named `hbtn_0c_0` if it doesn't already exist. |
| `2-remove_database.sql`   | Script to delete the database `hbtn_0c_0`. |
| `3-list_tables.sql`       | Script that lists all the tables of a database in MySQL. |
| `4-first_table.sql`       | Script that creates a table called `first_table` in the current database. |
| `5-full_table.sql`        | Script to create a table with multiple columns and types. |
| `6-list_values.sql`       | Script to list all records of a table. |
| `7-insert_value.sql`      | Script to insert a new record in a table. |
| `8-count_89.sql`          | Script that displays the number of records with `id = 89`. |
| `9-full_creation.sql`     | Script that creates a table and inserts a record in one command. |
| `10-top_score.sql`        | Script to list all records of a table sorted by score. |
| `11-best_score.sql`       | Script to list all records with a score >= 10. |
| `...`                     | Other scripts as per project tasks. |

## Usage

Scripts can be executed by running a command in the format:

```sh
mysql -hlocalhost -uroot -p < file_name.sql
