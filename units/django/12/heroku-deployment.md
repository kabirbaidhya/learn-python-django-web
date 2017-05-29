Deployment to Heroku
=====================
[Home](https://github.com/kabirbaidhya/learn-python-django-web) | [← Prev](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/django/11/rest-api.md) | [Next →]()

## Deployment
So far we've developed a todoapp with pretty much the basic features and have now finalized it. So, we'll be deploying the application to [Heroku](https://dashboard.heroku.com/apps).

## Before we begin
You need to [signup](https://signup.heroku.com/?c=70130000001x9jEAAQ) for a new account on Heroku if you haven't already. After you have an account, you also need to download the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) which we'll be using for deploying our application.

Here's how you [install](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) it.

## Login
Once you have your heroku account and the cli tool installed you can login to heroku via CLI.
```bash
$ heroku login
```

This will ask you for your credentials and will get you logged in.

## Adding more dependencies
We need to add few more dependencies which we'll need before deploying our application. But first make sure you already have activated your virtual environment.
```bash
$ source ~/envs/py3-django-pg/bin/activate
```

```bash
$ pip install dj-database-url gunicorn whitenoise python-dotenv psycopg2
```

## Read More

 1. https://www.heroku.com/
 2. https://devcenter.heroku.com/articles/deploying-python
 3. https://docs.djangoproject.com/en/1.11/howto/deployment/
 4. https://devcenter.heroku.com/articles/getting-started-with-python#introduction
 5. https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment
