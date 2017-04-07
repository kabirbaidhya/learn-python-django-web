<!--
$theme: gaia
template: invert-->
###### Database
Database & SQL (PostgreSQL)
==================

# ![](../../../python-logo-200x200.png)

###### [@kabirbaidhya](https://github.com/kabirbaidhya)

---
<!--
$theme: gaia
template: gaia-->
# Reflections
---
### So far,
We've covered all these things

1. Python Basics

<small>Note: If you're not aware of these. Read them at https://github.com/kabirbaidhya/learn-python-django-web</small>

---
# Before we begin
---
<!--
$theme: gaia
template: default-->
### Database

A structured repository of data held in a computer, for easier retrieval and manipulation.

---
### DBMS
A software that provides a systematic way to create, manage and work with databases.

Modern DBMSs are available generally in two types: **SQL/Relational Databases and NoSQL Databases**.

Well-known DBMSs: MySQL, PostgreSQL, MongoDB, MariaDB, Microsoft SQL Server, etc.

---
### Table
A table is a structured collection of data about a specific entity in a database. In a relation database, data is organized in terms of relations or tables.

---
### Table
A table consists of rows (records) and columns (fields). Each row in a table consists of a complete information about an instance of the entity related with the table eg: a user. And each column of the row is a specific attribute of that particular entity eg: user's name or email.

---
<!--
$theme: gaia
template: invert-->
### For example
<small>A table with data about users would look like:</small>
<small>

id |    name    |       email        
---|------------|--------------------
 1 | Test User  | foo@bar.com
 2 | Test User  | foo@bar.com
 4 | New User 1 | newuser1@gmail.com
 5 | New User 2 | newuser2@gmail.com
 6 | New User 3 | newuser3@gmail.com
 7 | New User 4 | newuser4@gmail.com
 8 | New User 5 | newuser5@gmail.com
 9 | New User 6 | newuser6@gmail.com

</small>

---
<!--
$theme: gaia
template: default-->
### Primary Key
A Primary Key (PK) is a special column (or combination of columns) in a table which uniquely identifies each record in the table.

The value of PK column:
1. Must be UNIQUE across all the records in the table.
2. Must not contain NULL values.

---
<!--
$theme: gaia
template: gaia-->
# SQL
---
<!--
$theme: gaia
template: default-->
### SQL
SQL(Structured Query Language) is the defacto language for managing, retrieving, & manipulating data and databases in the relational database world.

The SQL language consists entire vocabulary for database management, querying, insertion, manipulation or removal of data in relational databases.

---
<!--
$theme: gaia
template: invert-->
### For example
This is an example SQL query that retrieves a list of users whose emails start with `foo@`:

```
SELECT * FROM users WHERE email LIKE 'foo@%';
```

The result set that is retrieved would look like this:

<small>

id |    name    |       email        
---|------------|--------------------
 1 | Test User  | foo@bar.com
 2 | Test User  | foo@bar.com
 
</small>

---
<!--
$theme: gaia
template: gaia-->
# PostgreSQL
---
<!--
$theme: gaia
template: default-->
### PostgreSQL
> PostgreSQL is a powerful, open source object-relational database system.

<small>As per https://www.postgresql.org/about/</small>


---
### PostgreSQL
PostgreSQL is one of the most popular and reliable choice in the relational database world along with MySQL, Oracle & Ms SQL Server.

---
### Why PostgreSQL?
1. Modern relational database
2. 15+ years of active development
3. Strong reputation for reliability, data integrity, and correctness
4. Open source
5. An enterprise class database with proven architecture

---
---
<!--
$theme: gaia
template: gaia-->
###### This slide was a part of course
####  Python, Django & Web Development
###### [github.com/kabirbaidhya/learn-python-django-web](https://github.com/kabirbaidhya/learn-python-django-web)
---
# Thank You
###### [@kabirbaidhya](https://github.com/kabirbaidhya)
###### kabirbaidhya@gmail.com
<!--footer: The slides were created using Marp. https://yhatt.github.io/marp/ -->
