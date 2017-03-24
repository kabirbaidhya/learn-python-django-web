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
print fib(50)
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

## Using the `main()` function
Although python gives you full flexibility to structure your code as you like. It is recommended that you make your code organized and modular. And you can make use of functions for that.

While you already do write functions for each of the logical actions, tasks or computations you do. You still need to write some code to trigger or kickstart them when your program starts. In many programming languages like C/C++ or even java, they strictly enforce you to define a `main()` function for that particular purpose. Although python doesn't enforces you to do the same, it is actually a good practice to do have a something like `main` function to make your code more readable and organized.

For instance:
You can do the fibonacci series from our earlier example like this:

```python
def fib(n):
    a, b = 0, 1

    while a < n:
        print(a)
        (a, b) = (b, a + b)


def main():
    n = int(input('N = '))

    # Print the series upto n
    print fib(n)


# Now this is what triggers everything
# when the program starts.
main()
```

## Lambdas
A lambda is a short anonymous function that can be used in expressions and easily passed as arguments to other function calls.

For example:

This is a simple function that computes a product of two numbers:
```python
def product(a, b):
    return a * b

c = product(2, 5)
```
Now you can do the same using `lambda` function as well.
```python
c = (lambda a, b: a * b)(2, 5)
```
This creates an anonymous function on the fly to compute the product and invokes it immediately with the arguments 2 and 5.
If this is hard for you to understand. You can do it like this as well.
```python
func = lambda a, b: a * b
c = func(2, 5)
```
Here we're doing the exact same thing; the only difference is that we're using an intermediate variable `func` to store the lambda function and use it to compute the value of c in the next line.

Lambda functions are pretty handy tool when you make use of a lot of higher order functions and closures. Especially while doing functional programming, lambdas become pretty common.

#### Example 5
This program will demonstrate a very basic use case of lambda functions.

```python
# A function that returns another function
# to add a number with another number
def get_adder_of(a = 1):
    return lambda x: x + a

add_five = get_adder_of(5)
add_two = get_adder_of(2)
add_seven = get_adder_of(7)

print('10 + 5 = %d' % add_five(10))
print('8 + 2 = %d' % add_two(8))
print('8 + 7 = %d' % add_seven(8))
```

#### Example 6
This is another use case of a lambda function.

```python
my_list = [1, 2, 3, 4, 5]

# Using map() function and lambda to
# get a new list of squares of the original list.
squares = list(map(lambda x: x ** 2, my_list))
# The same thing could be achieved using list comprehension.
squares_2 = [x ** 2 for x in my_list]

print(squares)
print(squares_2)
```

## Exercises
Do all the exercises we've done so far in previous lessons using functions to wrap up the logic.

Guidelines:
 1. Write the primary logic of the program using function(s).
 2. Do not invoke the functions directly. Use a `main()` function instead.
 3. Protip Read user inputs and print the outputs in the `main()` function keeping just the core logic in the other functions.

## Read More?
Want to read more? Go through these links.
1. http://www.cs.utah.edu/~germain/PPS/Topics/functions.html
2. https://docs.python.org/3/tutorial/controlflow.html
3. https://www.tutorialspoint.com/python/python_functions.htm
4. http://stackoverflow.com/questions/9450656/positional-argument-v-s-keyword-argument
