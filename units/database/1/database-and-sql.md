Database and SQL
================
[Home](https://github.com/kabirbaidhya/learn-python-django-web) | [Slides](https://speakerdeck.com/kabirbaidhya/python-classes-and-objects) | [← Prev](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/python/8/classes-and-objects.md) | [Next →]()

This is a very short and concise tutorial that quickly introduces the concepts of relational databases, SQL & PostgreSQL to help the beginners be familiar with developing database-driven
applications in the later lessons to come. For more in-depth resources follow the links on the [Read More](#) section below.

## Terms and Terminologies
Before we begin with PostgreSQL we need to be (at least) aware of what the following terms and terminologies mean.

### Database

A structured repository of data held in a computer, for easier retrieval and manipulation.

### DBMS
A software that provides a systematic way to create, manage and work with databases.

Modern DBMSs are available generally in two types: **SQL/Relational Databases and NoSQL Databases**. We'll focus more on Relational Database concepts here. If you want to know more about NoSQL databases check [this](http://nosql-database.org/).

Well-known DBMSs include MySQL, PostgreSQL, MongoDB, MariaDB, Microsoft SQL Server, etc.

### Table
A table is a structured collection of data about a specific entity in a database. In a relation database, data is organized in terms of relations or tables.

A table consists of rows (records) and columns (fields). Each row in a table consists of a complete information about an instance of the entity related with the table eg: a user. And each column of the row is a specific attribute of that particular entity eg: user's name or email.

For instance: This is an example of database table with data about users:


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


### Primary Key
A Primary Key (PK) is a special column (or combination of columns) in a table which uniquely identifies each record in the table.

It is one of the important [database constraints](http://stackoverflow.com/questions/2570756/what-are-database-constraints) used in relational databases.

In our above example table the `id` attribute is the PK.
The value of PK column:
1. Must be UNIQUE across all the records in the table.
2. Must not contain NULL values.

Read More about Primary Key [here](https://technet.microsoft.com/en-us/library/ms191236.aspx).


### SQL
SQL(Structured Query Language) is the defacto language for managing, retrieving, & manipulating data and databases in the relational database world.

The SQL language consists entire vocabulary for database management, querying, insertion, manipulation or removal of data in relational databases.

For example:
This is an example SQL query that retrieves a list of users whose emails start with `foo@`:

```
SELECT * FROM users WHERE email LIKE 'foo@%';
```

The result set that is retrieved would look like this:


id |    name    |       email        
---|------------|--------------------
 1 | Test User  | foo@bar.com
 2 | Test User  | foo@bar.com

Common SQL statements include: `CREATE DATABASE`, `CREATE TABLE`, `SELECT`, `UPDATE`, `INSERT`, `DELETE`.
We'll discuss about the most common SQL statements and queries below.

## PostgreSQL
> PostgreSQL is a powerful, open source object-relational database system. It has more than 15 years of active development and a proven architecture that has earned it a strong reputation for reliability, data integrity, and correctness.

<small>As per https://www.postgresql.org/about/</small>

PostgreSQL is one of the most popular and reliable choice in the relational database world along with MySQL, Oracle & Ms SQL Server.


Why PostgreSQL?
1. Modern relational database
2. 15+ years of active development
3. Strong reputation for reliability, data integrity, and correctness
4. Open source
5. An enterprise class database with proven architecture


### Installation
Linux/Unix/Mac users: check the [detail instructions here](https://wiki.postgresql.org/wiki/Detailed_installation_guides)

Windows users: follow [these steps](http://www.postgresqltutorial.com/install-postgresql/)

## Database Management
Database management generally means Creation, Administration, Granting Permissions, Schema Manipulation and Troubleshooting of Databases using a DBMS.

Here's we'll see how we can create databases and tables in PostgreSQL.

### PostgreSQL CLI Client
PostgreSQL comes with the standard CLI client to manage and connect to databases in the PostgreSQL server.

After installing PostgreSQL correctly. You can run it with `psql` command.

### Creating a database
You can use standard SQL `CREATE` statement to create a database.

**Syntax**
```sql
CREATE DATABASE database_name;
```

For example, this will create a database `my_db`:
```sql
CREATE DATABASE my_db;
```

You can also create a database using the `createdb` command which comes with postgresql.
```
$ createdb my_db
```
This would do the same thing.

### Connecting to a database

If you're already inside the `psql` shell then you can use `\c` to connect to a database.

Like this:
```
$ psql
psql (9.5.6)
Type "help" for help.

kabir=# \c my_db;
You are now connected to database "my_db" as user "kabir".
my_db=#
```
If you're outside of `psql` shell, you can directly run psql by connecting to that database like this:

```
$ psql my_db
psql (9.5.6)
Type "help" for help.

my_db=#
```

Now all the SQL statements you run in this shell would run on the database `my_db`.

### Creating a table.
As we already know that table is the basic builing blocks in any relational database, let's go and create a table.

You can create a table using the `CREATE TABLE` SQL statement.


The basic syntax for `CREATE TABLE` is:

```sql
CREATE TABLE table_name (
	column1 TYPE_OF_DATA column_constraints,
	column2 TYPE_OF_DATA column_constraints,
    ...
	table_constraint
	table_constraint
    ...
);
```

Let's create a new table `users` with columns:
 - `id` - PK
 - `first_name` - String
 - `last_name` - String
 - `email` - String (Unique)
 - `address` - String
 - `password` - String
 - `created_at` - Date

The SQL statement could look like this:

```sql
CREATE TABLE users (
    id serial PRIMARY KEY,
    first_name varchar (20) NOT NULL,
    last_name varchar (20) NOT NULL,
    email varchar (50) NOT NULL UNIQUE,
    address varchar (100),
    password varchar (50) NOT NULL,
    created_at timestamp NOT NULL
);
```

This is a simple example of creating a table. For in-depth syntax for `CREATE TABLE` statement check [this](https://www.postgresql.org/docs/9.1/static/sql-createtable.html):

### Listing tables/relations/objects
You can do `\d` or `\d+` to list all the tables in the database inside `psql`.

It should show something like this:
```
my_db=# \d+
                          List of relations
 Schema |     Name     |   Type   | Owner |    Size    | Description
--------+--------------+----------+-------+------------+-------------
 public | users        | table    | kabir | 0 bytes    |
 public | users_id_seq | sequence | kabir | 8192 bytes |
(2 rows)
```

## CRUD Operations
The CRUD stands for Create, Read, Update, Delete that are the general database manipulation operations we do in database.

### Create
To create a new record in a table. We use the SQL `INSERT` statement.

**Syntax**
```sql
INSERT INTO users (column1, column2, ...)
VALUES (value1, value2, ...);
```

Let's try inserting a record in our last table:
```sql
INSERT INTO users (first_name, last_name, email, address, password, created_at)
VALUES ('Foo', 'Bar', 'foo@test.com', 'Kathmandu, Nepal', 'test', NOW());
```
Notice that we haven't mentioned the column `id` here because we've used the `serial` data type for it. It would be auto incremented by postgresql automatically when new record is inserted using sequences.

We can add some more:
```sql
INSERT INTO users (first_name, last_name, email, address, password, created_at)
VALUES
('Test 1', 'Test', 'test1@test.com', 'Kathmandu, Nepal', 'test', NOW()),
('Test 2', 'Test', 'test2@test.com', 'Kathmandu, Nepal', 'test', NOW()),
('Test 3', 'Test', 'test3@test.com', 'Kathmandu, Nepal', 'test', NOW());
```

Remember that we've added a UNIQUE constraint on the `email` column. Let's try adding a record with an existing email.
```psql
INSERT INTO users (first_name, last_name, email, address, password, created_at)
VALUES ('Foo New', 'Bar', 'foo@test.com', 'Kathmandu, Nepal', 'test', NOW());
```

You will get this error due to the violation of unique constraint on `email`:
```
ERROR:  duplicate key value violates unique constraint "users_email_key"
DETAIL:  Key (email)=(foo@test.com) already exists.
```

### Read
We use `SELECT` statement to retrieve or query the relations.

The basic syntax for `SELECT` just for retrieving all the records from a table is:
```sql
SELECT col1, col2, col3... FROM table_name;
```

If you execute this query, you will see the following results:
```sql
SELECT * FROM users;
```

```
 id | first_name | last_name |     email      |     address      | password |         created_at         
----+------------+-----------+----------------+------------------+----------+----------------------------
  1 | Foo        | Bar       | foo@test.com   | Kathmandu, Nepal | test     | 2017-04-07 07:03:08.196081
  2 | Test 1     | Test      | test1@test.com | Kathmandu, Nepal | test     | 2017-04-07 07:03:22.308518
  3 | Test 2     | Test      | test2@test.com | Kathmandu, Nepal | test     | 2017-04-07 07:03:22.308518
  4 | Test 3     | Test      | test3@test.com | Kathmandu, Nepal | test     | 2017-04-07 07:03:22.308518
(4 rows)
```

You can even select only a few columns like this:

```sql
SELECT first_name, last_name, email FROM users;
```
```
 first_name | last_name |     email      
------------+-----------+-----------------
 Foo        | Bar       | foo@test.com   |
 Test 1     | Test      | test1@test.com |
 Test 2     | Test      | test2@test.com |
 Test 3     | Test      | test3@test.com |
(4 rows)
```

The above syntax is a very minimal syntax for `SELECT` statement. However it could have much more complex syntax when it comes to querying the tables as per our need.
It could be like:

```sql
SELECT col1, col2,... FROM table_name, [table_name2, ...] [JOIN another table ...] [WHERE conditions] [GROUP BY ..] [HAVING ..] [ORDER BY col1, col2 ASC|DESC];
```

### Update
We use `UPDATE` statement to update record(s) on a table.
**Syntax**
```sql
UPDATE table_name SET col1 = value1, col2 = value2... WHERE condition;
```

Try this:
```
UPDATE users SET last_name = 'Test' WHERE email LIKE '%test.com';
```

Now if you check the records again, you should see this:
```
SELECT * FROM users;
```
```
 id | first_name | last_name |     email      |     address      | password |         created_at         
----+------------+----------------+----------------+------------------+----------+----------------------
  1 | Foo        | Test      | foo@test.com   | Kathmandu, Nepal | test     | 2017-04-07 07:03:08.196081
  2 | Test 1     | Test      | test1@test.com | Kathmandu, Nepal | test     | 2017-04-07 07:03:22.308518
  3 | Test 2     | Test      | test2@test.com | Kathmandu, Nepal | test     | 2017-04-07 07:03:22.308518
  4 | Test 3     | Test      | test3@test.com | Kathmandu, Nepal | test     | 2017-04-07 07:03:22.308518
(4 rows)
```

### Delete
We use `DELETE` statement to remove records(s) from a table.

## Exercises
**Syntax**
```sql
DELETE FROM table_name WHERE condition;
```

Try running this query and check the records again you'll see how it works.

```sql
DELETE FROM users WHERE id = 1 or id = 3;
```

Now if you check the records again, you should see 2 records have been removed:
```
SELECT * FROM users;
```
```
id | first_name |   last_name    |     email      |     address      | password |         created_at         
----+------------+----------------+----------------+------------------+----------+----------------------------
 2 | Test 1     | Test Test User | test1@test.com | Kathmandu, Nepal | test     | 2017-04-07 07:03:22.308518
 4 | Test 3     | Test Test User | test3@test.com | Kathmandu, Nepal | test     | 2017-04-07 07:03:22.308518
```

## Exercises
 1. Create a database: my_app
 2. Create tables:
    - The same `users` table like above.
    - todos
        - id
        - user_id       - Foreign key to users table
        - title         - String
        - description   - Text (can be NULL)
        - completed     - Boolean (defaults to false)
        - created_at    - timestamp
 3. Insert 5 users and 8 todos
 4. Write a SELECT query to retrieve a list of todo items with  following information:
    (id, title, description, user_id, user_name - concatenation of both first_name & last_name, completed, created_at). (Hints: Use `JOIN`)

## Read More?
Want to read more? Go through these links.
1. https://www.postgresql.org/docs/9.6/static/tutorial-start.html
2. http://www.postgresqltutorial.com/
3. http://nosql-database.org/
4. http://stackoverflow.com/questions/2570756/what-are-database-constraints
5. https://technet.microsoft.com/en-us/library/ms191236.aspx
6. https://www.digitalocean.com/community/tutorials/how-to-create-remove-manage-tables-in-postgresql-on-a-cloud-server
