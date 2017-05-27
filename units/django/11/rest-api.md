REST API Development
=====================
[Home](https://github.com/kabirbaidhya/learn-python-django-web) | [← Prev](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/django/10/hashtags.md) | [Next →]()

## API Development
So far we've covered about developing a CRUD Web Application using Django and we have used a traditional MVC approach on developing the TodoApp. Now we'll see how we can expose a REST API for our TodoApp.

To understand more about what REST is, you can check this [stackoverflow thread](https://stackoverflow.com/questions/671118/what-exactly-is-restful-programming#answer-671132).

## Setting Up
Firstly we'll need to add a new package `djangorestframework` into our django application. As django by default isn't REST friendly for developing application we need to add this new package to make developing RESTful applications easier.

```bash
$ pip install djangorestframework
```

After you've installed this, go and add `rest_framework` on the `INSTALLED_APPS` list in the `settings.py` file:
```python
INSTALLED_APPS = [
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'todos'
]
```

## Serialization
Since our REST API is going to be fully JSON based, we'll need to add serializer classes which will automatically handle the serialization/deserialization task for us.

So, go and create a new file `serializers.py` under our `todos` directory:

```python
from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    ''' Serializer to map the Todo model to JSON. '''

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Todo
        fields = ('id', 'title', 'description', 'completed', 'created_at', 'user')
        read_only_fields = ('created_at', 'id')
```
In the above code, we've just created a new serializer `TodoSerializer` for our `Todo` model class.

## Adding a ListView
In RESTful API routes there are generally two kinds of endpoints: collection endpoints and resource endpoints. 

The collection endpoints are those which would return a list of resources on `GET` and which would create a new resource on `POST` and other HTTP verbs like `OPTIONS`, `HEAD` etc are supported as always.

Our our TodoApp todos collection endpoint would look like this:
```
GET     /api/todos
POST    /api/todos
```
So, to handle these we'll create a new view `TodoListView` since it's a collection endpoint. Go to your `views.py` and add a new class `TodoListView`.

```python
from rest_framework import generics
from todos.models import Todo
from todos.serializers import TodoSerializer

class TodoListView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
```

Now this view will be responsible for creating a new todo item when it gets a `POST` request with payload and will return a list of todo items (in JSON) when it gets a `GET` request.

We'll still need to add a new url that points to this view, let's add this new url for `/api/todos` in our `urls.py` file:

```python

from todos import views

urlpatterns = [
    ...
    url(r'^api/todos$', views.TodoListView.as_view(), name='api_todo_list')
]
```
Now that we have our todo list API ready, let's go and test it using Postman.

You can go and send a `GET` request on `http://localhost:8000/api/todos` and you should receive a list of todo items in JSON as a response.

And if you try a `POST` request on the same url `http://localhost:8000/api/todos` with a JSON payload of data you want to create, you'll see that it creates a new item.


## Read More

 1. https://www.slideshare.net/beveganbevegan/rest-46394978
 2. http://www.django-rest-framework.org/#tutorial
 3. https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-1
