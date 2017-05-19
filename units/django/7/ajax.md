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

## Using the JSON API
Now that we've created our new update HTTP API on the server side, we'll need to be able to hit that API from our client-side JavaScript asynchronously in the background, this is what Ajax means.

And we'll need to do that to update the completed status of the todo item when user changes the checked state of the checkbox for the todo items.

### Adding Axios JavaScript Library
We'll use [`axios`](https://github.com/mzabriskie/axios) http client library to do async http requests. So, first download it from `https://unpkg.com/axios@0.16.1/dist/axios.min.js`.

We'll put it in our `todos/static/todos` directory.

After you've downloaded the axios js file update your `base.html` to include that.

You can append this at the end of your `<body>` tag just above the `<script>` that includes our `todo.js` script.

```html
    ...
    <script src="{% static 'axios.min.js' %}"></script>
    <script src="{% static 'todos/js/todo.js' %}"></script>
</body>
...
```

### Handling checkbox change event
We'll need to add a handler to listen to the `change` event of our checkbox in the todo list. This is where we'll send request to our update API to update the completed state of the todo item.

And since we'll also need to know the `id` of the todo item we're updating we'll need to add id explicitly in all the checkboxes. So, we'll pass in the `id` in the django todolist template where we have our checkbox.

Find the `<input type="checkbox">` tag in your template and update the following.

```html
<input type="checkbox" {% if item.completed %}checked{% endif %} data-id="{{item.id}}" class="todo-complete-check" />
```
All we've done above is pass in the `id` of todo item as `data-id` attribute in the checkbox and give it a class `todo-complete-check`.

Now let's add a new even handler function in our `todo.js` file for this checkbox.
```javascript
function handleTodoCheckChange(e) {
    var checked = e.target.checked;
    var todoId = e.target.getAttribute('data-id');

    console.log('todo: ', todoId, checked);
    // TODO: Implement logic here.
}
```

We'll also need to register this event handler for the `change` event of the checkboxes. Since, we could have several different checkboxes we will register this for all of the checkboxes in loop like this.

```javascript
var checkboxes = document.querySelectorAll('.todo-complete-check');

if (checkboxes) {
    // Register check event handler for each checkbox
    for (var i = 0; i < checkboxes.length; i++) {
        checkboxes[i].addEventListener('change', handleTodoCheckChange);
    }
}
```

Now we'll need to register event handlers when the window has just finished loading. So, we'll add this code in the `handleLoad` function.

It should look like this now:
```javascript
function handleLoad() {
    var form = document.querySelector('.todo-form form');
    var messages = document.querySelector('.messages');
    var checkboxes = document.querySelectorAll('.todo-complete-check');

    if (checkboxes) {
        // Register check event handler for each checkbox
        for (var i = 0; i < checkboxes.length; i++) {
            checkboxes[i].addEventListener('change', handleTodoCheckChange);
        }
    }

    if (form) {
        form.addEventListener('submit', handleFormSubmit);
    }

    if (messages) {
        console.log('Message will be hidden after 5 seconds.');
        setTimeout(hideMessages, 5000);
    }
}
```

Now that we've added the event handlers to the checkboxes. If you refresh your browser, open the JavaScript console and try to check/uncheck the checkboxes in the todo list. You'll see the logs in the console, which ensures that our handlers are working now.

### Async HTTP requests
Now that we've added event handlers for the checkbox state change event. We'll need to trigger our JSON API that we've made to update the todo item completed status.

Since, we've already added axios library to our application, we can use it as the following.

```javascript
function handleTodoCheckChange(e) {
    var checked = e.target.checked;
    var todoId = e.target.getAttribute('data-id');
    var body = {'completed': checked};

    console.log('todo: ', todoId, checked);

    // Do a PATCH request with the completed data.
    console.log('Sending a PATCH request');

    axios.patch('/api/todos/' + todoId, body)
        .then(function(response) {
            console.log('Response received', response.statusText, response.data);
        });
}
```

The above code will send async http request to the `PATCH` endpoint we've created in our django backend application.

If you refresh your browser and try checking on/off the checkboxes you'll notice that it's actually working. You can also check the records in the database to verify if the todo items are really being updated or not.

## Source Code
Check the full source code [here](https://github.com/kabirbaidhya/django-todoapp/tree/step-22).

## Read More?
 1. https://docs.djangoproject.com/en/1.11/topics/http/decorators/
 2. https://simpleisbetterthancomplex.com/tutorial/2016/08/29/how-to-work-with-ajax-request-with-django.html
 3. https://developer.mozilla.org/en-US/docs/Web/Events/change
 5. https://www.sitepoint.com/developers-rest-api/
 4. https://github.com/mzabriskie/axios
 5. https://docs.brightcove.com/en/video-cloud/concepts/postman/postman.html
