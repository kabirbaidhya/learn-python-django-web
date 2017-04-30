Templates and Views
===================
[Home](https://github.com/kabirbaidhya/learn-python-django-web) | [← Prev](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/django/2/django-helloworld.md) | [Next →]()

In this tutorial we'll be adding more templates and design improvements on our todo application we built using django in the [previous tutorial](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/django/2/django-helloworld.md).

Here we'll be mostly working with the UI of the todoapp using django template tags, html & css to finish our app's looks.

We'll start with the following steps:

1. Create a new url route for "Create TODO" page and link it with the Add button.
2. Extract a base template the app from `index.html`.
3. Add a new template for the create form.
4. Add template for the TODO list.
5. Add actions (Edit/Remove) for each of the TODO item on the list.
6. Display the actions (Edit/Remove) only when the TODO items are hovered.
7. Render the todo list dynamically using a list of todo items.
8. Strike-through and fade the completed items.
9. Add a new url for saving the TODO items.
10. When Add form is saved:
    - Create a new TODO item.
    - Redirect back to the index page.
11. Create a new url for the TODO edit page and display edit page when "Edit" link is clicked.
12. When Edit form is saved:
    - Save the changes made on the edited item.
    - Redirect back to the index page.

Check the full source code [here](https://github.com/kabirbaidhya/django-todoapp).
