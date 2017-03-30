Modules and Packages
============================

[Home](https://github.com/kabirbaidhya/learn-python-django-web) | [Slides](https://speakerdeck.com/kabirbaidhya/python-modules-and-packages) | [← Prev](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/python/6/exception-handling.md) | [Next →]()

## Modules
Modules in Python are nothing just plain python files with `.py` extension that may contain and expose a set of definitions be it functions, classes, variables, etc.

Definitions from one module can be imported to other modules and so on which helps in code reusability.

Of course you can think of functions when you want to create reusable logic in your code. But you need some kind of wrapper or namespacing that would wrap your functions and definitions to avoid naming collisions as there could be many functions with the same name. And this is where modules come into play. Modules provide all of these. It provides a wrapper for your functions or any other definitions and plus provide you a namespace for you. And you can import your functions from one module in other modules pretty easily, taking the code reusability provided by functions to the next level.

You can use `import` statement to import a module or the definitions from a module in another module.

Consider the following example.

#### Example 1
Create a file `util.py` with the following code:

```python
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


def fibo(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b

    return result
```

This is simply a python module that contains two functions `factorial` & `fibo`.

Now let's create another module, a main module which we will execute directly. Let's name it `main.py`.

```python
import util # Import the util module here


def main():
    n = input('Enter a Number: ')

    series = util.fibo(n).join(', ')
    print('Fibonacci Series up to {}: \n {}'.format(n, series))
    print('Factorial of {}'.format(n, util.factorial(n)))


main()
```

As simple as that. I think that explains you what modules in python actually are.

## More on Modules
You application generally is composed of several different modules. All of your modules may contain both executable and non-executable code (like function definitions, class definitions etc.) but it's usually preferable to keep all your executable code only in your main module or the module that you're using as an entry point script and make all the other modules have only non-executable code.

But this might not be the case all the time. Sometimes you may want modules with a combination of both executable and non-executable code.

Or, you may want to conditionally check if the module is run directly as an entry-point script or is imported in other modules to trigger some executable code.

### Module's `__name__`
In every module you define you can find a `__name__` variable whose value would be the name of the module.
When you run a module directly as a script, the value of `__name__` inside that module is set to `__main__` otherwise it's value would be the module's name.

Look at this example below.

#### Example 3
```python
import sys

def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()


if __name__ == '__main__':
    n = int(sys.argv[1])
    fib(n)
```

Save this module as `fib.py`:

Now you can use this file both as a script and an importable module.

#### Running it directly
To execute this script directly you can do:

```bash
$ python fib.py 100
```
This would take the value of `n` from the command line arguments and run the program. The code executes and prints the output since here the value of `__name__` will be `__main__`.

#### Importing it on other modules
Now if you try importing this module into other module. The executable code i.e the code under the `if __name__ == '__main__'` block won't be executed. Instead it will be executed when the  function `fib` is called in the module in with `fib` is imported. Check this:

```python
import fib

n = int(input('Enter N: '))
# Now execute that function.
fib.fib(n)
```

This is because, here the value of `__name__` inside the fib module won't be set to `__main__` again as it was not executed direclty but imported in a different module. So, now the above module which you'll execute directly will have it set as `__main__` instead. And the `fib` module will have the value of `__name__` set to it's name i.e `fib`.

In this way, you may know if the module is run directly as a script or is imported as a module.

## Variants of the `import` syntax
There are few ways you can use the `import` statement in python.

This is the most basic one which imports the module itself in it's own name.
```python
import fib
```
So, to access the `fib` function defined inside the `fib` module you need to do
```python
>>> fib.fib(50)
```

Another way is to use `from ... import` syntax like this,
```python
from fib import fib
```

This would just import the function `fib` from the module `fib`.
Now to call the `fib` function you can directly do `fib()` instead of doing `fib.fib()` like above.
This would be helpful if you only need one or two functions from a module.

You can import multiple definitions from a module like this:
```python
from foo import bar, baz, test, xyz
```
Here only the names mentioned would be imported.

Lastly, you can also import all the names that a module defines using,
```python
from foo import *
```

This will import everything that has been defined in the `foo` module. But this is not considered a good practice and not recommended either.

## Compiled python modules
Loading python modules does impact the performance a little bit as it's an IO operation. To speed up loading modules, Python caches the compiled version of each module. So, when they're imported they usually import the cached or already compiled version of your code instead of the real module. Python 3.x and above stores these compiled byte-code files under `__pycache__` directory and Python 2.x stores them as `.pyc` files just along with the source files.

When you have multiple modules in your application, you will notice these files after you run your program.

## Built-in modules
Python provides it's standard library as a set of modules and packages as well. Let's look into this simple example.

#### Example 2
```python
import math

value = 5.34

print('value =', value)
print('ceil =', math.ceil(value))
print('floor =', math.floor(value))
print('abs =', math.fabs(value))
```

Here we're using the [`math`](https://docs.python.org/3/library/math.html) module which is one of the built-in modules that python has in it's [standard library](https://docs.python.org/3/library/).

Actually there are many built-in modules & packages available out of the box in python's standard library. You can check the full list [here](https://docs.python.org/3/library/).

## Read More?
Want to read more? Go through these links.
 1. https://docs.python.org/3/tutorial/modules.html
 2. https://python.swaroopch.com/modules.html
 3. https://docs.python.org/3/library/
