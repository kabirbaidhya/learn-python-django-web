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

## Fixtures
### Create fixtures for todos
We now have a table to store our data. But it's all empty right now, let's add some dummy data so that we can test them.

Create a directory `fixtures` under the `todos` folder and add a file `todos/fixtures/todos.json` with the following data:
```json
[
    {
        "model": "todos.todo",
        "pk": 1,
        "fields": {
            "title": "Item 1",
            "completed": false,
            "description": "No eam nisl assum impetus, dicta .",
            "created_at": "2017-05-01 05:08:08.407942+05:45"
        }
    },
    {
        "model": "todos.todo",
        "pk": 2,
        "fields": {
            "title": "Item 2",
            "completed": true,
            "description": "No eam nisl assum impetus, dicta .",
            "created_at": "2017-05-02 05:08:08.407942+05:45"
        }
    },
    {
        "model": "todos.todo",
        "pk": 3,
        "fields": {
            "title": "Item 3",
            "completed": false,
            "description": "No eam nisl assum impetus, dicta .",
            "created_at": "2017-05-03 05:08:08.407942+05:45"
        }
    },
    {
        "model": "todos.todo",
        "pk": 4,
        "fields": {
            "title": "Item 4",
            "completed": false,
            "description": "No eam nisl assum impetus, dicta .",
            "created_at": "2017-05-04 05:08:08.407942+05:45"
        }
    },
    {
        "model": "todos.todo",
        "pk": 5,
        "fields": {
            "title": "Item 5",
            "completed": false,
            "description": "No eam nisl assum impetus, dicta .",
            "created_at": "2017-05-05 05:08:08.407942+05:45"
        }
    }
]
```

### Load fixtures
Once you've created your fixtures file `todos.json`, you can load the data into the database using:
```bash
 ➜ python manage.py loaddata todos
```

When it's done, you can try running the following commands in your `psql` shell you should get the results like these:
```plain
todoapp=# SELECT * FROM todos_todo;
 id | title  |            description             | completed |            created_at            
----+--------+------------------------------------+-----------+----------------------------------
  2 | Item 2 | No eam nisl assum impetus, dicta . | t         | 2017-05-02 05:08:08.407942+05:45
  3 | Item 3 | No eam nisl assum impetus, dicta . | f         | 2017-05-03 05:08:08.407942+05:45
  5 | Item 5 | No eam nisl assum impetus, dicta . | f         | 2017-05-05 05:08:08.407942+05:45
  4 | Item 4 | No eam nisl assum impetus, dicta . | t         | 2017-05-04 05:08:08.407942+05:45
  1 | Item 1 | No eam nisl assum impetus, dicta . | t         | 2017-05-01 05:08:08.407942+05:45
(5 rows)
``` 
## Django Shell
Django comes with an interactive shell, just like the shell or [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) we have for python. In this shell we can not just run regular python statements but also import our application's packages and try out our app's internal modules & packages.

Let's try it out by running:
```
 ➜ python manage.py shell
```
Now in this shell you can try the following things:
```python
>>> from todos.models import Todo
>>> todos = Todo.objects.all()
<QuerySet [<Todo: Todo object>, <Todo: Todo object>, <Todo: Todo object>, <Todo: Todo object>, <Todo: Todo object>]>

>>> todos[0]
<Todo: Todo object>

>>> todos[0].title
'Item 1'

>>> todos[0].description
'No eam nisl assum impetus, dicta .'

>>> todo = Todo.objects.get(pk=2)

>>> todo
<Todo: Todo object>

>>> todo.title
'Item 2'

>>> todo.description
'No eam nisl assum impetus, dicta .'

```

## Dynamic data in the views
Now that we have our `Todo` model all setup and have the database with some existing data, we can now load the todo items directly from our database in our views and eventually display in the html. 

Using django's models this becomes a trivial task. Open your `todos/views.py` file and update your `index` route with the following code:
```python
from todos.models import Todo

def index(request):
    items = Todo.objects.all()

    return render(request, 'index.html', {'items': items})
```

In the above code we've done:
```python
items = Todo.objects.all()
```
This will fetch all the todo items from the database and return an instance of `QuerySet` object that contains a list of all records we have in the database.

All it does behind the scenes is fire this query:
```sql
SELECT * FROM todos_todo;
```
and return the rows.

Now run your server using:
```bash
 ➜ python manage.py runserver
```

And check the app in your browser, you should be able to see that our todo list is now retrieved from the database. 

Check the full source code [here](https://github.com/kabirbaidhya/django-todoapp/tree/step-16).

## Read More?
Go through the following links if you want to learn more about Django Models, ORM & database stuff in django.
1. https://docs.djangoproject.com/en/1.11/topics/db/models/
2. https://docs.djangoproject.com/en/1.11/ref/models/instances/#django.db.models.Model
3. https://docs.djangoproject.com/en/1.11/howto/initial-data/
4. https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04
5. https://docs.djangoproject.com/en/1.11/topics/db/queries/
6. http://stackoverflow.com/questions/5394331/how-to-setup-postgresql-database-in-django



