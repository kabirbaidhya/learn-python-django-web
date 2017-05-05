Database, ORM and Models
========================
[Home](https://github.com/kabirbaidhya/learn-python-django-web) | [← Prev](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/django/3/templates-and-views.md) | [Next →]()

In our [previous tutorial]((https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/django/3/templates-and-views.md)) we finished the UI for our todoapp using django templates, views and urls. But we used hard-coded data while building the UI, in this tutorial we'll using a postgresql database to store our data and will see how we can make use of Django ORM & Models to retrieve data from our tables.

Here we'll be mostly working with the UI of the todoapp using django template tags, html & css to finish our app's looks.

## Database Setup
### New Database creation
Firstly we'll need to start by creating a new postgres database like what we did in one of our previous tutorial on [databases and sql](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/database/1/database-and-sql.md). You can go and check that first if you're still new to postgres.

Run the postgres client `psql`.
```bash
 ➜ psql
psql (9.5.6)
Type "help" for help.
```

Create a new database `todoapp`.
```sql
CREATE DATABASE todoapp;
```

### Database Configuration in Django
Now we need to configure our new postgres database in django. Firstly, install a new package `psycopg2` using `pip`. 
**Note:** This has to be installed in the same `virtualenv` that we've created for this project in the first django tutorial previously.

```bash
 ➜ pip install psycopg2
```

Now open the `settings.py` file from our project and make these following changes to the `DATABASES` constant as per your database credentials.

It should look like this:
```python
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'myproject',
            'USER': 'myprojectuser',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
```

### Migrations
Since, we've just setup our new database. It's just an empty database now, we need to run migrations to populate the django default tables into our database. 

Let's run the migrations then.
```bash
 ➜ python manage.py migrate
```

If you're migrations are done. You can go and check the database using `psql` directly to verify that the tables are created now.

Run `psql` in the CLI providing database `todoapp`.
```bash
 ➜ psql todoapp
```
Now, in the `psql` interactive shell you can run the `\d` to list all the tables. You should be able to see something like this:
```plain
todoapp=# \d
                       List of relations
 Schema |               Name                |   Type   | Owner 
--------+-----------------------------------+----------+-------
 public | auth_group                        | table    | kabir
 public | auth_group_id_seq                 | sequence | kabir
 public | auth_group_permissions            | table    | kabir
 public | auth_group_permissions_id_seq     | sequence | kabir
 public | auth_permission                   | table    | kabir
 public | auth_permission_id_seq            | sequence | kabir
 public | auth_user                         | table    | kabir
 public | auth_user_groups                  | table    | kabir
 public | auth_user_groups_id_seq           | sequence | kabir
 public | auth_user_id_seq                  | sequence | kabir
 public | auth_user_user_permissions        | table    | kabir
 public | auth_user_user_permissions_id_seq | sequence | kabir
 public | django_admin_log                  | table    | kabir
 public | django_admin_log_id_seq           | sequence | kabir
 public | django_content_type               | table    | kabir
 public | django_content_type_id_seq        | sequence | kabir
 public | django_migrations                 | table    | kabir
 public | django_migrations_id_seq          | sequence | kabir
 public | django_session                    | table    | kabir
(19 rows)
```
Now this means our database has been all set.

## Models
In Django, a model is the single source of information about the data. It contains the attributes and behaviors of the data that are being stored in the database. A Model is an ORM layer abstraction of the underlying database table and each model generally maps to a single table in the database.

Few things to make sure in django are:
1. Each model should be a subclass of `django.db.models.Model` class.
2. Each model attribute maps to the corresponding table attribute.

You can read more about Django Models if you like [here](https://docs.djangoproject.com/en/1.11/topics/db/models/).

The following could be an example of Django Model.
```python

from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    created_at = models.DateTimeField()
```

### Create a new Model
Let's create a new Model `Todo` for storing our todo items in the database. 
Write the following code in your `todos/models.py` file:

```python
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField()
```

### Generate migrations
Let's generate migration files for our new model by running.
```bash
 ➜ python manage.py makemigrations
```
This will generate migration files for our new `Todo` model.

### Run Migrations
Now we need to run these migrations to create the corresponding schema for our model.
```bash
 ➜ python manage.py migrate
```
Everytime we create a new model or make changes to the existing ones, we'll need to create migrations and run them to sync our database with our models.

After the migrations are done, you can go and check if a table for our `Todo` model has been generated or not. It should be there with the name `todos_todo`.

You can do `\d+` in the psql shell:
```
todoapp=# \d+ todos_todo;
                                                        Table "public.todos_todo"
   Column    |           Type           |                        Modifiers                        | Storage  | Stats target | Description 
-------------+--------------------------+---------------------------------------------------------+----------+--------------+-------------
 id          | integer                  | not null default nextval('todos_todo_id_seq'::regclass) | plain    |              | 
 title       | character varying(50)    | not null                                                | extended |              | 
 description | text                     |                                                         | extended |              | 
 completed   | boolean                  | not null                                                | plain    |              | 
 created_at  | timestamp with time zone | not null                                                | plain    |              | 
Indexes:
    "todos_todo_pkey" PRIMARY KEY, btree (id)
```
You can see how corresponding table and the columns are auto-generated by the migrations.



Check the full source code [here](https://github.com/kabirbaidhya/django-todoapp/tree/step-16).

## Read More?
Go through the following links if you want to learn more about Django Models, ORM & database stuff in django.
1. https://docs.djangoproject.com/en/1.11/topics/db/models/
2. https://docs.djangoproject.com/en/1.11/ref/models/instances/#django.db.models.Model
3. https://docs.djangoproject.com/en/1.11/howto/initial-data/
4. https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04
5. https://docs.djangoproject.com/en/1.11/topics/db/queries/
6. http://stackoverflow.com/questions/5394331/how-to-setup-postgresql-database-in-django



