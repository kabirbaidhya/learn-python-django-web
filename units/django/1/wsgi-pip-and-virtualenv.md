WSGI, pip and virtualenv
========================
Before we directly jump into Web Development (backend) with Django we need to be familiar with few concepts and tools. In this session we're going to be discussing about them.

## pip
[`pip`](https://packaging.python.org/key_projects/#pip) is a package manager used to install and manage packages in the python world. Real world applications compose of many different dependencies, third-party libraries/packages maintaining them manually along with their dependencies could be a hassle. Thankfully we have package managers like pip to the rescue. 

If you are a Linux user you might be familiar with the tools like `apt-get`, `yum` etc. you can think of `pip` as similar tool for managing application level packages for python projects.

You can read about installing pip [here](https://packaging.python.org/installing/#requirements-for-installing-packages).

Once you have `pip` installed, you can verify it with:
```
$ pip --version
```
It should print the version something like this:
```plain
pip 9.0.1 from /usr/local/lib/python2.7/dist-packages (python 2.7)
```

Now let's try installing a popuplar CLI tool made in python [`httpie`](https://httpie.org/) using pip.

```bash
$ pip install httpie
```

## virtualenv
Virtualenv is another popular tool used in the python community. It is used to create virtual environments for python projects such that each one can have a different version of Python, and a different sets of libraries.

Imagine a situation where you have to work on a project that relies upon python 2.7 but you also have another project that uses python 3.5. Virtualenv helps us maintain such different environments.

### Installation

You can install `virtualenv` using `pip` like this:

```bash
$ pip install virtualenv
```

Now test your installation:
```
$ virtualenv --version
```

## WSGI
WSGI is one of the common term that you should come across when you're beginning Web Development using Python. So, what does WSGI mean? WSGI stands for Web Server Gateway Interface. 

WSGI is nothing but a standard specification how Web Servers should communicate with Web applications written in Python. Almost all the popular web based frameworks like Django or Flask are WSGI compliant and follows the spec. 

As web frameworks are built on top of the WSGI spec, you'll be able to understand how these frameworks work behind the scenes after learning about WSGI.

### WSGI - Hello World

Let's try a hello world example to see what WSGI is all about.

Create a new file `hello.py`:
```python
from wsgiref.simple_server import make_server


def application(env, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, headers)

    return [b'Hello World']

# Instantiate the server
PORT = 8000
httpd = make_server('localhost', PORT, application)

print("Server is listening on port", PORT)
# Serve the HTTP requests
httpd.serve_forever()

```

Here we've created a simplest WSGI based HTTP server that would send back "Hello World" to the HTTP Clients when requested.

Now let's run by: 
```bash
$ python hello.py
```

You should see the output:
```
Server is listening on port 8000
```

This means our simples http server has started listening for http requests on port 8000. Let's try opening this url [http://localhost:8000](http://localhost:8000) in the browser to see the response.

You should see the output "Hello World" printed on your browser. 
Great. You just created a simplest web server in python.

Now let's try sending a request to our server using `httpie` CLI tool.

```bash
$ http GET http://localhost:8000
```

You should now see the whole http response sent by our server:
```plain
HTTP/1.0 200 OK
Content-Length: 11
Content-Type: text/plain
Date: Thu, 27 Apr 2017 20:24:28 GMT
Server: WSGIServer/0.2 CPython/3.5.2

Hello World
```

### WSGI - Hello World with HTML
Now let's try sending html content instead of just plain text.

First let's create a new python script `hello_html.py`:
```python
import os
from wsgiref.validate import validator
from wsgiref.simple_server import make_server


def application(env, start_response):
    # Read the html from the file
    html = read_html('html/hello.html')

    # Convert it to byte string
    html = html.encode('ASCII')

    headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(html)))
    ]
    start_response('200 OK', headers)

    return [html]


def read_html(filename):
    directory = os.path.dirname(os.path.realpath(__file__))
    full_path = os.path.join(directory, filename)
    f = open(full_path)
    data = f.read()
    f.close()

    return data

# Instantiate the server
PORT = 8051
httpd = make_server('localhost', PORT, application)

print("Server is listening on port", PORT)
# Serve the HTTP requests
httpd.serve_forever()

```
Similarly let's create a directory `html` in the current directory and let's add a file `hello.html` inside it.

Save the file `html/hello.html` with the following contents:
```html
<html>
  <head>
    <title>Hello World!</title>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>
```

By checking the above code you might have already understood what we're going to do here. All we're doing is just sending the contents of the file `html/hello.html` to the browsers as `Content-Type: text/html`.

Now, let's run this server and see the output in the browser just like what we did before.

```bash
$ python hello_html.py
```
After you see this line printed in the CLI:
```
Server is listening on port 8000
```
You can check the url [http://localhost:8000](http://localhost:8000) in your browser and you'll be able to see "Hello World" as a Web page in your browser.

You can also try this with `httpie`, you should get the following output:
```plain
 ➜ http GET http://localhost:8000
HTTP/1.0 200 OK
Content-Length: 110
Content-Type: text/html
Date: Thu, 27 Apr 2017 20:35:24 GMT
Server: WSGIServer/0.2 CPython/3.5.2

<html>
  <head>
    <title>Hello World!</title>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>
```

This was the basic web server implemented using just WSGI that sends out responses as html content.

## Read More?
1. http://wsgi.readthedocs.io/en/latest/
2. https://www.fullstackpython.com/wsgi-servers.html
3. https://pip.pypa.io/en/stable/
4. https://packaging.python.org/key_projects/#pip
5. http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/
