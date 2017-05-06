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

## Forms
Now that we know how to create or manipulate our data. We need to work on our forms so as to allow our users to create and update data using them. 

### Create Todo Form
We already have setup a page with the create todo form previously now we're going to make it fully functional. Before doing that we need to add a new url to which the form will be submitted to.

#### Add a new url
So, we'll start by adding a new url `save` to our `todos/urls.py` file, which should look like this:

```python
from django.conf.urls import url
from todos import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create$', views.create, name='create'),
    url(r'^save$', views.save, name='save')
]
```
#### Add a new view function
Now we'll also need to add `views.save` function that we're referenced above, which should look like this:

```python
from django.shortcuts import render, redirect

def save(request):
    # TODO: Logic to save the todo item here.

    return redirect('index')
```

Currently, the above code does nothing but just redirect back to `index` page url. But here we need to get the data received from the form, save it and then finally redirect to index.

### Saving the form data
Let's update the `save` function we've just created to receive data from the form and save it using our `Todo` model. The code should look like this:

```python
from django.shortcuts import render, redirect
from django.utils import timezone
from todos.models import Todo

def save(request):
    # Get the form data from the request.
    title = request.POST.get('title')
    description = request.POST.get('description')

    # Create a new todo item with the data.
    Todo.objects.create(
        title=title,
        description=description,
        created_at=timezone.now()
    )

    # Redirect back to index page
    return redirect('index')

```

### Updating the HTML form
We now need to update our HTML form to submit the data properly to the server like what we've expected in the above code.

We'll need to ensure the following things:
 1. Form should be submitted to url `save` (`name='save'`).
 2. Form should be submitted using method `POST`
 3. Two form fields are required to be sent `title` and `description` for the todo item.
 4. And CSRF token should be sent along with the form too.

After making these changes to our plain html form it should look like this:
```html
{% extends 'base.html' %} 
{% block content%}
<h3>Add Todo</h3>
<div class="todo-form">
    <form method="post" action="{% url 'save' %}">
        {% csrf_token %}
        <div class="form-group">
            <label for="input-todo-title">Title</label>
            <input type="text" name="title" class="form-control" id="input-todo-title" placeholder="What do you want to do?">
        </div>
        <div class="form-group">
            <label for="description">Description</label>
            <textarea name="description" class="form-control" id="description" placeholder="Description"></textarea>
        </div>

        <button type="submit" class="btn btn-primary">Save</button>
    </form>
</div>
{% endblock %}
```

## Source Code
Check the full source code [here](https://github.com/kabirbaidhya/django-todoapp/tree/master).

## Read More?
