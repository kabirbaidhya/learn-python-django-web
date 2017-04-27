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

Imagine a situation where you have to work on a project that relies upon python 2.7 but you also have another project that uses python 3.5. Virtualenv helps us maintain such different enironments.

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

## Read More?
1. http://wsgi.readthedocs.io/en/latest/
2. https://www.fullstackpython.com/wsgi-servers.html
3. https://pip.pypa.io/en/stable/
4. https://packaging.python.org/key_projects/#pip
5. http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/
