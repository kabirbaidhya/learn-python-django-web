Validation
========================
[Home](https://github.com/kabirbaidhya/learn-python-django-web) | [← Prev](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/django/5/form-processing.md) | [Next →]()

In the [previous tutorial](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/django/5/form-processing.md) we've learned how we can create and update the todo item using the forms. But we haven't added any validation in our forms nor in the backend to prevent any invalid data to go into our database. In this tutorial we're going to cover that part.

Generally in any web application whenever we're taking in user input, we need to validate the data first and this has to be done both on the frontend (client-side) and on the backend (server-side). We'll see how we can do that here.

## Backend Validation
Backend validation is important regardless of the fact that whether data is already validated on the client ordjango.contrib not.

In our todoapp the validation logic would be very simple as we have only few fields. 
Let's add a logic to validate data in our `views.py` before the data gets saved.

The validation logic would look like this:
```python
    # Validation logic
    if title is None or title.strip() == '':
        messages.error(request, 'Item not saved. Please provide the title.')
        return redirect(request.META.get('HTTP_REFERER'))
```
After adding this to our existing code, our `save` function would look like this:

```python
from django.contrib import messages

def save(request):
    # Get the form data from the request.
    title = request.POST.get('title')
    description = request.POST.get('description')

    # Get hidden form data.
    form_type = request.POST.get('form_type')
    id = request.POST.get('id')

    print('Form type received:', form_type)
    print('Form todo id received:', id)

    # Validation logic
    if title is None or title.strip() == '':
        messages.error(request, 'Item not saved. Please provide the title.')
        return redirect(request.META.get('HTTP_REFERER'))

    if form_type == 'create':
        # Create a new todo item with the data.
        todo = Todo.objects.create(
            title=title,
            description=description,
            created_at=timezone.now()
        )
        print('New Todo created: ', todo.__dict__)
    elif form_type == 'edit' and id.isdigit():
        todo = Todo.objects.get(pk=id)
        print('Got todo item: ', todo.__dict__)

        # Save logic
        todo.title = title
        todo.description = description

        todo.save()
        print('Todo updated: ', todo.__dict__)

    # Add save success message
    messages.info(request, 'Todo Item Saved.')
    # Redirect back to index page
    return redirect('index')
```

Now that we've added a validation logic in our `view.py`, we need to display the validation messages in our templates too.

Firstly, create a new template `templates/messages.html` that would be responsible for displaying these messages.
```html
{% if messages %}
<div class="alert alert-info" role="alert">
    <ul class="messages list-unstyled">
        {% for message in messages %}
        <li{% if message.tags %} class="{{ message.tags }}" {% endif %}>
            {{ message }}
            </li>
            {% endfor %}
    </ul>
</div>
{% endif %}
```

Now, we'll need to include it in our `form.html` template just below the `<h3>` heading tag.
```html
<h3>
    {% if form_type == 'create' %}
        Add Todo
    {% elif form_type == 'edit' %}
        Edit Todo
    {% endif %}
</h3>
{% include 'messages.html' %}
```

Now if you refresh the application in the browser and try to save the form with empty title, you should see the validation message in the form.

Great. We've just added the backend validation before saving.

## Frontend Validation
We know validating the user's data in the backend is really crucial. But when it comes to User Experience(UX) it might feel slow, as the form has to be submitted to the server first and then server would send back the error. 

The user experience could feel really bad if there are too many fields in the form and the internet connection is poor, that way if the validation errors occur in the backend the user will be keep on redirected to the form only after the whole form has been submitted and validated on the server.

To make this better, we can validate the data on the client side using javascript too and that will be before submitting the form.

For that we will add a new javascript file to our application. Create a new file `todo.js` under `static/todos/js`.

```javascript
window.addEventListener('load', handleLoad);

function handleLoad() {
    var form = document.querySelector('.todo-form form');

    if (form) {
        form.addEventListener('submit', handleFormSubmit);
    }
}

function handleFormSubmit(e) {
    var titleInput = document.querySelector('#input-todo-title');
    var title = titleInput.value.trim();

    if (!title || title === '') {
        alert('Please enter the title.');
        titleInput.focus();
        e.preventDefault();
    }
}
```

This code should prevent the form from submission if the title is empty. 

Don't forget to include this javascript file to our html template `base.html` in order to load it.

You can put this tag inside the `<body>` tag at the last.
```html
        <footer class="footer">
            <p>&copy; 2016 Company, Inc.</p>
        </footer>

    </div>
    <!-- /container -->
    <script src="{% static 'todos/js/todo.js' %}"></script>
</body>
```
Now you can refresh your browser and test the application by trying to submit the form with empty title field. You should get the javascript `alert` saying `'Please enter the title.'`.

### HTML5 validation
Now a final step to complete the frontend validation would be to add HTML5 validation attributes like `required` to your input tags.

Let's add `required` attribute to our `<input>` tag for title. It should look like this.
```html
<input type="text"
    name="title" class="form-control"
    id="input-todo-title"
    placeholder="What do you want to do?"
    value="{{todo.title}}"
    required
/>
```

## Source Code
Check the full source code [here](https://github.com/kabirbaidhya/django-todoapp/tree/step-20).

## Read More?
 1. https://docs.djangoproject.com/en/1.11/ref/forms/validation/#using-validators
 2. https://docs.djangoproject.com/en/1.11/ref/templates/builtins/
 3. https://docs.djangoproject.com/en/1.11/ref/contrib/messages/
 5. https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms
