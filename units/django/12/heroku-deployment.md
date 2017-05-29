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

Now you'll need to write down all your application dependencies to a `requirements.txt` using:
```bash
$ pip freeze > requirements.txt
```

## Add a Procfile
You'll need to create a new file `Procfile` in the root of your project with the following contents.
```
web: gunicorn todoapp.wsgi --log-file -
```

Heroku will use this file to run your application.

## Static files configuration

Now we'll need to make few tweaks to our application config and settings before we can deploy it.

Open your `settings.py` file and replace the line 
```python
STATIC_URL = '/static/'
```
with these contents
```python
ALLOWED_HOSTS = ['*']
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    # os.path.join(PROJECT_ROOT, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
```

Also, make few changes in your `wsgi.py` file by adding `whitenose` initialization code something like this:

```python
import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoapp.settings')

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
```

## Database Configuration
Furthermore, in the `settings.py` add the following lines below your database configuration,
```python
# Update database configuration with $DATABASE_URL.
import dj_database_url

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
```

Your database configuration should look similar to this now.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
    }
}

# Update database configuration with $DATABASE_URL.
import dj_database_url

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
```

Here we've configured to set the database details using the `DATABASE_URL` environment variable which heroku will set for us when we setup our postgres database on heroku.

So, for our local development environment it would just take the database credentials using our predefined parameters and on heroku it will use the `DATABASE_URL` env variable.

## Read More

 1. https://www.heroku.com/
 2. https://devcenter.heroku.com/articles/deploying-python
 3. https://docs.djangoproject.com/en/1.11/howto/deployment/
 4. https://devcenter.heroku.com/articles/getting-started-with-python#introduction
 5. https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment
