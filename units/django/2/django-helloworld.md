Django - Hello World
====================
[Home](https://github.com/kabirbaidhya/learn-python-django-web) | [← Prev](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/django/1/wsgi-pip-and-virtualenv.md) | [Next →]()

In this session we're going to dive into the [django](https://www.djangoproject.com/) framework and create our very first project using django.

Here we'll try to create a TodoApp. I hope by now you're pretty clear about the [basics](https://github.com/kabirbaidhya/learn-python-django-web#python) and the concepts of [web](https://github.com/kabirbaidhya/learn-python-django-web#web-development-basics), [wsgi and some pythonic tools](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/django/1/wsgi-pip-and-virtualenv.md) we've discussed in our [previous sessions](https://github.com/kabirbaidhya/learn-python-django-web) so far, if not then you might want to check these links.

## TodoApp
Now let's start building our app.

### Setup virtualenv
Let's start by setting up `virtualenv` with Python 3+.

We'll create a virtualenv named `py3` under `envs` directory.
```bash
 ➜ mkdir ~/envs
 ➜ virtualenv -p /usr/local/bin/python3 ~/envs/py3
```

Now activate it.
```bash
 ➜ source ~/envs/py3/bin/activate
```
You should now be able to see a virtualenv identifier `py3` near your prompt in the terminal like this:
```bash
(py3) 
[kabir@leapfrog] ~
 ➜ 
```
