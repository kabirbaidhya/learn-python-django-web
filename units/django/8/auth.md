Django Authentication and Admin
===============================
[Home](https://github.com/kabirbaidhya/learn-python-django-web) | [← Prev](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/django/7/ajax.md) | [Next →]()

In this tutorial we'll try to build a login and user authentication system in our todo application.

## Step by Step Instructions

We'll do following tasks step-by-step for building the user login and authorization system.

 1. Create a login page.
    - Add a new url for the login page
    - Create a login form template
    - Create a view function to render the login page
    - Add a link in the home page to go to login

 2. Authenticate the user when login form submitted
    - Add a new url for login form submission.
    - Add a new view function to login and authenticate the user.
        - It should redirect the user to home page if login was successful.
        - It should redirect to the same for if login failed and show messages.
    - Hide the login link if user has been logged in.
    - Display the username instead of the Login in the header if user is logged in.

 3. Create a signup page.
   - Add a new url for the signup page
   - Create a signup form template
   - Create a view function to render the signup page
   - Add a link in the home page to go to signup

 4. Authorization
    - Allow only the logged in users to view the todo list
    - Allow only the logged in users to view the Add todo form
    - Allow only the logged in users to edit the Todo item
    - Allow only the logged in users to delete the Todo item
    - Allow only the logged in users to view the home page. So, redirect the user to login if user is not logged in.

## Read More

 1. https://docs.djangoproject.com/en/1.11/topics/auth/default/#how-to-log-a-user-in
 2. https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
