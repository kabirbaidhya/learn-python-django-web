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

## Create a new app
Now that setup our application for deployment do commit all your changes to the `master` branch of your repository.

And create a new app on heroku by using the command:
```bash
$ heroku create django-todoapp
```

This command will create a new application on heroku `django-todoapp`. 
**Note:** The app name `django-todoapp` should already be occupied so give a different name. Or, even if you omit the app name by just using `heroku create` it would select a random name for you.

## Add a PostgreSQL database
Add a postgresql database to the application on heroku.
```bash
$ heroku addons:create heroku-postgresql:hobby-dev
```

Now that we've created our app and the database you can go and see them in the [Heroku Dashboard](https://id.heroku.com/login) after login.

## Deploy
We're all set for deployment now. Now deployint to heroku is super easy, just push your master branch to the `heroku` remote and it will handle the rest for you.

```bash
$ git push heroku master
```

You would see the following output similar to this.

```
 ➜ git push heroku master 
Counting objects: 4, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 395 bytes | 0 bytes/s, done.
Total 4 (delta 3), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Python app detected
remote: -----> Installing requirements with pip
remote: 
remote: -----> $ python manage.py collectstatic --noinput
remote:        /app/.heroku/python/lib/python2.7/site-packages/dotenv/main.py:24: UserWarning: Not loading  - it doesn't exist.
remote:          warnings.warn("Not loading %s - it doesn't exist." % dotenv_path)
remote:        122 static files copied to '/tmp/build_34e7863071464e51736c94588a92fe6d/todoapp/staticfiles', 168 post-processed.
remote: 
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote: 
remote: -----> Compressing...
remote:        Done: 56.7M
remote: -----> Launching...
remote:        Released v6
remote:        https://django-todoapp.herokuapp.com/ deployed to Heroku
remote: 
remote: Verifying deploy... done.
To https://git.heroku.com/django-todoapp.git
   6bf00b0..30af97f  master -> master
```

Now that we've pushed our code and deployed we need to run run migrations to complete the entire deployment process.

Use the following command to run migrations on the heroku's server.
```bash
$ heroku run python manage.py migrate
```

After you're done with the migrations. Go to `https://django-todoapp.herokuapp.com/` i.e `https://<your-app-name>.herokuapp.com` and you should be able to see your app is up and running on heroku.

## Source Code
Check the full source code [here](https://github.com/kabirbaidhya/django-todoapp/tree/step-30).

## Read More

 1. https://www.heroku.com/
 2. https://devcenter.heroku.com/articles/deploying-python
 3. https://docs.djangoproject.com/en/1.11/howto/deployment/
 4. https://devcenter.heroku.com/articles/getting-started-with-python#introduction
 5. https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment
