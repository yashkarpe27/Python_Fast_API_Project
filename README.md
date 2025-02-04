# Python_Fast_API_Project

## Pre-requisites
Please follow the steps below before you start the project
Make sure to have minimum python version as 3.11
Set up requirements.txt as dependency file with following dependencies
Pydantic (validations)
SqlAlchemy (ORM)
Use MySQL database as backend database

## About assignment
Create 4 APIs mainly list, info, add, update for Product
API /product/list – List all products with pagination of 10 records per page
API /product/{pid}/info – View information about the requested product ID
API /product/add – Adds new product to database
API /product/{pid}/update – Updates existing product with product ID to database

## Product table (DB structure)
Product ID – bigint, primay key, auto increment
Name – varchar(100)
Category – varchar(15) – enum (finished, semi-finished, raw)
Description - varchar(250)
Product image - varchar(max) – image URL
SKU - varchar(100)
Unit of measure - varchar(5) - enum(‘mtr’, ‘mm’, ‘ltr’, ‘ml’, ‘cm’, ‘mg’, ‘gm’, ‘unit’, ‘pack’)
Lead time - int(3) – lead time in days
Created date – timestamp
 Updated date - timestamp
