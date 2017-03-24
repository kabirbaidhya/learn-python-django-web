Functions and Lambdas
============================

[Home](https://github.com/kabirbaidhya/learn-python-django-web) | [Slides](https://speakerdeck.com/kabirbaidhya/python-functions-and-lambdas) | [← Prev](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/python/4/conditionals-and-loops.md) | [Next →]()


## Functions
A function is a block of code that performs a single action or performs some computation. Usually functions take in some input, process it and returns the output.

Functions makes our code organized as it encapsulates a task or an action by wrapping up the actual logic or statements inside it and by abstracting the internal complexities and details to perform the task.

In programming use of functions provide:
 - Modularity
 - Reusability
 - Maintainability
 - Separation of Concern
 - Better Code Organization

## Functions in Python

In python we can define a function with the following syntax:
```python
def function_name():
    STATEMENTS
```

If the function needs to accept parameters then it will have following syntax:
```python
def function_name(parameters):
    STATEMENTS
```

And as already stated before about blocks and indentation, **don't forget:**
1. The colon `:`, which actually starts the function block.
2. Indentation, which is the part of syntax in python and a must have (unlike C-style languages where it's optional).
3. End of indent means end of the block.

#### Naming Convention
In python it's a community wide convention to use `snake_case` (i.e lowercase with underscores to separate words) for naming functions and variables.

#### Example 1
This could be an example of a function that computes sum of two numbers.
```python
def sum(x, y):
    return x + y
```

#### Example 2
And similarly this could be an example of a function which returns the maximum in between two numbers.

```python
def max(a, b):
    if a > b:
        return a

    return b

# Print maximum value
print max(5, 6)
```

#### Example 3
The earlier example can be done using the inline conditional operator like this:
```python
def max(a, b):
    return a if a > b else b

# Print maximum value
print max(5, 6)
```

#### Example 4
Function to print the fibonacci series.
```python
def fib(n):
    a, b = 0, 1

    while a < n:
        print(a)
        (a, b) = (b, a + b)

# Print the series
print max(50)
```

## Default Arguments
Python allows you to set default values for arguments to use in case when the user doesn't provide any value for these arguments while calling the function.

Assigning default values make the arguments act as optional parameters as they user can omit them while calling the function.

For instance:
```python
def greet(message = 'Hello'):
    return message + ' World!'

# Invoke this function
print greet()       # Hello World!
print greet('Hi')   # Hi World!
```

## Function Invocation
Calling/invoking the function is as simple as
```python
sum(5, 6)
```

Parentheses are the must haves when it comes to functions, both during definition and invocation.
Not all functions do have parameters. But when they do,  you need to invoke them with arguments inside parentheses as well.

It should be noted that all parameters (arguments) in python are passed by reference in Python.

In python, you can call a function using positional arguments, keyword arguments or a combination of both.

### Positional Arguments
Calling a function with positional argument means calling it by providing the arguments in the order they're defined as parameters in the function.

For instance:
```python
def sum(x, y, z = 0):
    return x + y + z

# Call using positional arguments
sum(1, 2, 3)        # 3 positional arguments
sum(1, 5)           # 2 positional arguments for x & y, z takes the default value 0
```

### Keyword arguments
Functions can also be called using keyword arguments using the parameter names in the form `arg=value`.

For instance:

```python
def sum(x, y, z = 0):
    return x + y + z

# Call using keyword arguments
sum(x=1, y=2, z=3)        # keyword arguments
sum(y=5, z=1, x=4)        # position of args doesn't matter here.
sum(x=1, y=5)             # 2 keyword arguments for x & y, z takes the default value 0
```

### Combine both positional and keyword arguments
You can call functions using both the positional and keyword arguments. But you need to ensure keyword arguments must follow positional arguments. No argument should receive a value more than once.

```python
sum(1, y=3, z=5)
sum(5, 6, z=10)
sum(10, y=2)
```

## Read More?
Want to read more? Go through these links.
1. http://www.cs.utah.edu/~germain/PPS/Topics/functions.html
2. https://docs.python.org/3/tutorial/controlflow.html
3. https://www.tutorialspoint.com/python/python_functions.htm
4. http://stackoverflow.com/questions/9450656/positional-argument-v-s-keyword-argument
