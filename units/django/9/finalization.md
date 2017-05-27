TodoApp Finalization
=====================
[Home](https://github.com/kabirbaidhya/learn-python-django-web) | [← Prev](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/django/8/auth.md) | [Next →]()

In this tutorial we'll try to finalize the todo app.

## Step by Step Instructions
 1. Display "No items in the list" message if there are no items in the todo list.
 2. Display the todo-items only for the logged in users.
    - Link the todo item with the user.
        - Add a new attribute `user` in the `Todo` model that references to the `User` model.
        - Create migration and run it.
    - Set the current user while saving the todo item.
    - Display only the user-specific todo items in the todo list. The list should display items created by the logged in user.
 3. Restrict non-creator users to edit the todo item.
 4. Restrict non-creator users to delete the todo item.
 5. Display custom message on a custom 404 Not Found page.


## Read More

 1. https://docs.djangoproject.com/en/1.11/topics/auth/default/#how-to-log-a-user-in
 2. https://docs.djangoproject.com/en/1.11/topics/db/models/
