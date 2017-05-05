Form Processing
========================
[Home](https://github.com/kabirbaidhya/learn-python-django-web) | [← Prev](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/django/4/database-orm-and-models.md) | [Next →]()

In the previous tutorial we've used integrated our app with the database and introduced the concept of Django Models. Also, 
we used the `Todo` model to fetch all the todo items from the database and display it on the UI dynamically. In this tutorial we'll go one step further, by adding a feature to allow creating a new todo item from the form and also allow editing an existing todo item.

## Create/Update data
In the previous tutorial, we've seen how we can use `Todo.objects.all()` method to get the list of todo items from the database. Now we're concerned about how we're going to create them or update them. 
However using Django's Models, these tasks become much easier. Let's try these in the django shell.

```bash
 ➜ python manage.py shell
```

### Creating a new entry
Creating a new todo item is as simple as calling `Todo.objects.create` method.

```python
>>> from django.utils import timezone
>>> timezone.now()
datetime.datetime(2017, 5, 5, 23, 35, 37, 755504, tzinfo=<UTC>)
>>> todo = Todo.objects.create(title='Yet another todo', created_at=timezone.now())
>>> todo.__dict__
{'description': None, 'title': 'Yet another todo', 'completed': False, 'created_at': datetime.datetime(2017, 5, 5, 23, 36, 12, 106900, tzinfo=<UTC>), 'id': 8, '_state': <django.db.models.base.ModelState object at 0x7f5202736240>}
```

### Updating the entry
Updating it is also simple as this.
```python
>>> todo.title = 'Just another todo'
>>> todo.description = 'Just a todo item'
>>> todo.save()
```

Now go and check the database you should be able to find your table has been updated.

```
todoapp=# SELECT * FROM todos_todo;
 id |       title       |            description             | completed |            created_at            
----+-------------------+------------------------------------+-----------+----------------------------------
  1 | Item 1            | No eam nisl assum impetus, dicta . | f         | 2017-05-01 05:08:08.407942+05:45
  2 | Item 2            | No eam nisl assum impetus, dicta . | t         | 2017-05-02 05:08:08.407942+05:45
  3 | Item 3            | No eam nisl assum impetus, dicta . | f         | 2017-05-03 05:08:08.407942+05:45
  4 | Item 4            | No eam nisl assum impetus, dicta . | f         | 2017-05-04 05:08:08.407942+05:45
  5 | Item 5            | No eam nisl assum impetus, dicta . | f         | 2017-05-05 05:08:08.407942+05:45
  8 | Just another todo | Just a todo item                   | f         | 2017-05-06 05:21:12.1069+05:45
(6 rows)
```

## Source Code
Check the full source code [here](https://github.com/kabirbaidhya/django-todoapp/tree/master).

## Read More?
