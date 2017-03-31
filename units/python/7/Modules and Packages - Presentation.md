<!--
$theme: gaia
template: invert-->
###### Python
Modules and Packages
==================

# ![](../../../python-logo-200x200.png)

###### [@kabirbaidhya](https://github.com/kabirbaidhya)

---
<!--
$theme: gaia
template: gaia-->
# Reflections
---
### So far,
We've covered all these things

1. Python Basics, Conditionals and Loops
2. Functions and Exception Handling

<small>Note: If you're not aware of these. Read them at https://github.com/kabirbaidhya/learn-python-django-web</small>

---
# Modules
---
<!--
$theme: gaia
template: default-->
### What are Modules?

Modules in Python are nothing just plain python files with `.py` extension that may contain and expose a set of definitions be it functions, classes, variables, etc.

Definitions from one module can be imported to other modules and so on which helps in code reusability.

You can use `import` statement to import a module or the definitions from a module in another module.

---

### What modules offer?
- Namespacing - avoid naming colisions of definitions
- Portability
- Even better code reusability
- Better Code Organization
- Modularity - Of Course

---
<!--
$theme: gaia
template: invert-->

###### Example 1
<small>This is a file (module) named `test.py`. </small>
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

---
###### Example 1
<small>This is another file (module) `main.py` that uses functions from `test` module.</small>

```python
import test # Import the test module here


def main():
    n = input('Enter a Number: ')

    series = test.fibo(n).join(', ')
    print('Series upto {}: \n {}'.format(n, series))
    print('Factorial of {}'.format(n, test.factorial(n)))


main()
```

---
### More on Modules

You application generally is composed of several different modules. Modules may contain both executable and non-executable code (like function definitions, class definitions etc).

But it's usually preferable to keep all your executable code only in your main module or the module that you're using as an entry point script and make all the other modules have only non-executable code.

---
### Module's `__name__`
In every module you define, you can find a `__name__` variable whose value would be the name of the module.

When you run a module directly as a script, the value of `__name__` inside that module is set to `__main__` otherwise it's value would be the module's name.

---
###### Example 2

```python
# fib.py
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

<small>You can use this file both as a script and an importable module.</small>

---
###### Example 2 - Running it directly
Run the script from command line

```bash
$ python fib.py 100
```

<small>This would take the value of `n` from the command line arguments and run the program. The code executes and prints the output since here the value of `__name__` will be `__main__`.
</small>

---
###### Example 2 - Importing as a module

```python
import fib

n = int(input('Enter N: '))
# Now execute that function.
fib.fib(n)
```
<small>Now if you're importing the module like this, the executable code under the `if __name__ == '__main__'` block won't be executed.

Instead it will be executed when the  function `fib` is called. </small>


---
# The `import` Syntax Variants
---
##### Syntax 1
<small>rts the module itself in it's own name.</small>
```python
import fib
```
<small>So, to access the `fib` function defined inside the `fib` module you need to do</small>
```python
>>> fib.fib(50)
```
---
##### Syntax 2
<small>Imports the function `fib` from the module `fib`.</small>

```python
from fib import fib
```

<small>Now to call the `fib` function you can directly do</small>
```python
>>> fib(50)
```

<small>You can also import multiple definitions from a module.</small>
```python
from foo import bar, baz, test, xyz
```

---
##### Syntax 3
<small>Imports all the names that the module defines</small>
```python
from foo import *
```

<small>**Note:** This is not considered a good practice and not recommended either.</small>

---
### Built-in Modules
Python provides it's standard library as a set of modules and packages. Let's look into this simple example.

There are many built-in modules & packages available out of the box in python's standard library. You can check the full list [here](https://docs.python.org/3/library/).

---
###### Example 3
<small>Using python's built-in `math` module</small>
```python
import math

value = 5.34

print('value =', value)
print('ceil =', math.ceil(value))
print('floor =', math.floor(value))
print('abs =', math.fabs(value))
```

<small>Here we're using the [`math`](https://docs.python.org/3/library/math.html) module which is one of the built-in modules that python has in it's [standard library](https://docs.python.org/3/library/).</small>

---
<!--
$theme: gaia
template: gaia-->
# Packages
---
<!--
$theme: gaia
template: default-->
### Packages in Python
If you think of the modules as files having `.py` extension; then you can think of packages as directories that contains modules.

Most importantly to be a package the directory, must contain a special file `__init__.py` which indicates python that it's a package that contains modules.

---
<!--
$theme: gaia
template: invert-->
##### Example 4
<small>For instance, consider the following directory structure:</small>

```
foo/
  __init__.py
  bar
    __init__.py
    baz.py
```

<small>Here `foo` is the main package, `bar` is the sub-package under `foo` and `baz.py` is a module inside `bar`.</small>

---
##### Example 4
<small>Let's say `baz.py` has the following code:</small>
```python
def say_hello(to = 'World'):
    print('Hello', to)
```

---
##### Example 4

<small>Now to reference the `baz` module from outside you would use the `import` statement with dotted names like this:</small>
```python
import foo.bar.baz

# You can call the say_hello() using
foo.bar.baz.say_hello()
```

<small>Alternatively you can use the `import .. from` syntax like this:</small>
```python
form foo.bar.baz import say_hello

say_hello('Again')
```
---
<!--
$theme: gaia
template: invert-->
# Let's do some real coding :)
---
<!--
$theme: gaia
template: gaia-->
##### Building a Simple App
## User Information App
#### Phase I
---
##### Please follow this link for the steps.
###### https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/python/7/modules-and-packages.md

---
<!--
$theme: gaia
template: gaia-->
# Read More?
---
<!--
$theme: gaia
template: default-->
### Links
Want to read more? Go through these links.
 1. https://docs.python.org/3/tutorial/modules.html
 2. https://python.swaroopch.com/modules.html
 3. https://docs.python.org/3/library/
 4. https://docs.python.org/3/library/json.html#module-json
 5. https://docs.python.org/3/library/functions.html#open

---
<!--
$theme: gaia
template: gaia-->
###### This slide was a part of course
####  Python, Django & Web Development
###### [github.com/kabirbaidhya/learn-python-django-web](https://github.com/kabirbaidhya/learn-python-django-web)
---
# Thank You
###### [@kabirbaidhya](https://github.com/kabirbaidhya)
###### kabirbaidhya@gmail.com
<!--footer: The slides were created using Marp. https://yhatt.github.io/marp/ -->
