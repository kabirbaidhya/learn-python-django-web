REST API Development
=====================
[Home](https://github.com/kabirbaidhya/learn-python-django-web) | [← Prev](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/django/10/hashtags.md) | [Next →]()

## Slides
Slides [here](https://www.slideshare.net/beveganbevegan/rest-46394978).

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

## Adding a list view
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

### Using Postman for testing
Now that we have our todo list API ready, let's go and test it using Postman.

#### Retrieving
You can go and send a `GET` request on `http://localhost:8000/api/todos` and you should receive a list of todo items in JSON as a response.

#### Creating
And if you try a `POST` request on the same url `http://localhost:8000/api/todos` with a JSON payload of data you want to create, you'll see that it creates a new item.

## Adding an item view
With the above `TodoListView` we are able to add `Create` and `Read` of CRUD functionality in our TodoApp using REST API.
Now we also need to be able to `Update`, `Delete` and `Read` individual todo items to complete all the CRUD operations for the todolist.

To to this, we'll have to create a new API endpoint which we'll be a resouce endpoint unlike the collection endpoint we've created above.

For this we'll add a new view class in our `view.py` file, `TodoItemView`:

```python
class TodoItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
```

Now, this new view will be responsible for updating, retrieving and deleting individual todo items using the REST API.

Finally, we'll need to add a new url that would point to this new view when a resource endpoint is hit. 

The endpoint will have to be something like `/api/todos/:id` that supports methods `GET`, `PUT`, `PATCH` and `DELETE`.
```
GET     /api/todos/:id
PUT     /api/todos/:id
PATCH   /api/todos/:id
DELETE  /api/todos/:id
```
This new endpoint will need to have `id` (Primary Key) as it needs to know which resource is going to be manipulated or retrieved.

For this endpoint we'll add the following urn patten in our `urls.py` file:
```python
urlpatterns = [
    ...
    url(r'^api/todos$', views.TodoListView.as_view(), name='api_todo_list'),
    url(r'^api/todos/(?P<pk>[0-9]+)$', views_api.TodoItemView.as_view(), name='api_todo_item')
]
```

Now that we have both list and item endpoints ready for the todolist, we have exposed the full CRUD functionalities of our application into REST Api endpoints.

### Using Postman for testing
Using Postman let's tryout this new endpoint `/api/todos/:id`.

#### Retrieving
Do a `GET` request on `http://localhost:8000/api/todos/:id` with any todo item `id` you have in your database and you should receive the data for that particular todo item.

#### Updating
A `PATCH` request on the same url `http://localhost:8000/api/todos/:id` with a JSON payload of data for any item `id` will update the data in the database according to the data sent in the payload.

### Deleting
A `DELETE` request on the same url `http://localhost:8000/api/todos/:id` will delete the item in the database given by the provided `id`.

## Read More

 1. https://www.slideshare.net/beveganbevegan/rest-46394978
 2. http://www.django-rest-framework.org/#tutorial
 3. https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-1
