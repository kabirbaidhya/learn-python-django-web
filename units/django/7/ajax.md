Asynchronous HTTP Requests (Ajax)
========================
[Home](https://github.com/kabirbaidhya/learn-python-django-web) | [← Prev](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/django/6/validation.md) | [Next →]()

In the [previous tutorial](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/django/5/validation.md) we've covered the form validation part both in the frontend and the backend. In this tutorial we can use Async HTTP Requests or Ajax in our application.

## Ajax Requests
Ajax(Asynchronous JavaScript and XML) is a term to refer Asynchronous HTTP requests in the frontend world. It's asynchronous in the sense that, it provides a mechanism to send HTTP requests (from the client-side) to the server in the background without affecting/blocking the current page rendering or without having to reload the whole web page.

In this tutorial we'll be using Ajax requests to update the `completed` attribute of any todo item asynchronously without the whole page refresh, using JavaScript.

## Adding a JSON API endpoint
Before we can send HTTP requests to the server, we need to create a new url endpoint in our django app to accept it. In this case we don't need to return any HTML data from the server as we just need to update the todo item on the server and return. So, here we'll create a url endpoint that accepts JSON data and responds with JSON too.

We'll be refering this new url endpoint as an API endpoint because it's different from the urls where HTML forms are synchronously submitted to or the urls where the users navigate directly, but instead it's just an API provided by the server to the client to do some operations based upon HTTP. So, we'll call it JSON API for now. 

### Add a new view
First, we'll add a new file `todos/views_api.py`. Here we will have a function `update` which will be responsible for handling our API request on the server.

```python
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from todos.models import Todo


@csrf_exempt
@require_http_methods(['PATCH'])
def update(request, id):
    # Get the params from the payload.
    data = json.loads(request.body.decode('utf-8'))

    print('Received update API request for todo id: ', id)
    print('Completed: ', data['completed'])

    # Update the model
    todo = Todo.objects.get(pk=id)
    todo.completed = data['completed']
    todo.save()

    print('Todo item updated')

    return JsonResponse({})

```

Here, we are using the HTTP `PATCH` method which might seem new to you as previously we're only used to `GET` and `POST` methods. We used `PATCH` here as this request will update our todo item partially which is as per the [HTTP spec](https://tools.ietf.org/html/rfc2068#section-19.6.1.1). 

We'll learn more about HTTP methods and JSON based APIs in later tutorials on REST APIs.

### Add a new url
Now that we've created a new view function, we'll create a new url for our update endpoint.

For this we'll make changes on our `todos/urls.py` file.
```python
from todos import views, views_api

urlpatterns = [
    ...
    url(r'^edit/todos/(\d+)$', views.edit, name='edit'),

    # API Route for Ajax
    url(r'^api/todos/(\d+)$', views_api.update, name='api_update_todo')    
]
```

### Testing the API
Now that our update API is ready to change the `completed` attribute of a todo item, we'll need to test it. For testing JSON based APIs or any HTTP APIs we can use tools like [postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en). It's a chrome web extension which you can install it on your chrome browser.

Go and install it first if you don't have it.

After you're done with installing, you can open the postman app.

Now in the postman, create a new tab and enter the following url:

```
http://localhost:8000/api/todos/2
```

I'm assuming you have already run the django dev server on port `8000`.

Also make sure you've provided the todo id of the todo item for which `completed` is `false`, so that we can test this API updates it to `true` with postman.

Now, since we're accepting only `PATCH` http method, set the method to `PATCH` from the dropdown near the url.

Our code above expects the request data to be JSON containing a boolean attribute `completed`. 
```python
    # Get the params from the payload.
    data = json.loads(request.body.decode('utf-8'))

    print('Received update API request for todo id: ', id)
    print('Completed: ', data['completed'])

    # Update the model
    todo = Todo.objects.get(pk=id)
    todo.completed = data['completed']
```

So, we'll provide a json data in postman like this:
```json
{
	"completed": true
}
```

Set the body to be raw JSON, paste the above json object in the request body and hit the Send button.

Now after you see the success response (`200 OK`) you can go and refresh you app in the browser, you can see our todo item with `id=2` has been updated with the checkbox checked as we've set `completed=true`. Now go back to the postman and change completed to `false` and hit Send again.

Now, if you come back to your browser and refresh you'll find it's completed attribute has been updated again. Great.

You can test this API for other todo items too just by changing the `id` value in the url to something else like this:
```
http://localhost:8000/api/todos/5
``` 


## Source Code
Check the full source code [here](https://github.com/kabirbaidhya/django-todoapp/tree/step-20).

## Read More?
