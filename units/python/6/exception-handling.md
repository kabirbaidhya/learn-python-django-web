Exception Handling
============================

[Home](https://github.com/kabirbaidhya/learn-python-django-web) | [Slides](https://speakerdeck.com/kabirbaidhya/python-exception-handling) | [← Prev](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/python/5/functions-and-lambdas.md) | [Next →](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/python/7/modules-and-packages.md)

## Exceptions
When there are errors in your syntax, your code won't run, that is for sure. But even if your syntax is 100% correct and runs fine, there could be cases when you get errors during the runtime of your program. These errors that get triggered in the runtime are called **Exceptions**.

For instance consider this example, when you're trying to divide two numbers, both received from the user input.

```python
a = float(input('First Number: '))
b = float(input('Second Number: '))

result = a / b
```
As the user can provide any values for the inputs, guess what happens when he provides the second value as zero. Obviously, it would throw an error. Yes, it would throw an error in the runtime named `ZeroDivisionError` and the program would halt.

There might me numerous cases like this when we detect errors only in the runtime which obviously causes unexpected termination of program with error.

We need to handle exceptions because unexpected termination of our program at the runtime due to some random error is certainly not what we want.

## Handling Exceptions
We can handle exceptions and runtime errors in python using `try` block.

Something like this:

```python
a = float(input('First Number: '))
b = float(input('Second Number: '))

try:
    result = a / b
except ZeroDivisionError:
    print('Error: Division by Zero')
```

Handling exceptions ensures that the program still continues to run regardless of the exceptions. To better understand this, consider the following improvement to the program where user can try again and the program continues to run until the user chooses to exit.

```python
while True:
    a = float(input('First Number: '))
    b = float(input('Second Number: '))

    try:
        result = a / b
        print('Result = {}'.format(result))

    except ZeroDivisionError:
        print('Error: Division by Zero')

    try_again = input('\nTry Again (Y/N)? ')

    # If the user doesn't want to try again exit the loop.
    if try_again.upper() != 'Y':
        break

    print()

# Program will exit finally
print('Good Bye!')
```

## The `try` statement
You've already seen how and why we use `try` statement. Let's get into details about how it actually works.

**Syntax**

```python
try:
    STATEMENTS
except SomeException:
    # Code to handle exception
```
Firstly the statements inside the `try` block are executed one by one. If any of the statement causes any exceptions the rest of the code in the block are skipped.

It will check if the exception which is raised is there in the `except` clause or not. If yes, then that particular except block is executed.

In case the exception raised is not in the `except` clause it will propagate to the higher level. If that particular exception has no handler even after reaching the highest level then the program terminates with that exception with it's message shown.

If no exception occurs inside the `try` block after execution of the statements in the code block, the `except` blocks are skipped.

#### Example 1
Consider the following example we did in our previous lesson.

```python
n, sum = 0, 0

while n < 5:
    value = input('Enter Number %s: ' % (n + 1))
    sum = sum + float(value)
    n += 1

print('Sum = %.2f' % sum)
```

This program expects numeric values from the user. Guess what would happen if the user supplies a non-numeric value in the prompt. Go and try it with some input like `abx`, `xyz` etc.

You'll get an error like this:
```plain
Traceback (most recent call last):
  File "units/python/4/example_5.py", line 7, in <module>
    sum = sum + float(value)
ValueError: could not convert string to float: 'abc'
```

Now here's the improved version of this program where we've handled this exception.
```python
n, sum = 0, 0

while n < 5:
    value = input('Enter Number %s: ' % (n + 1))

    try:
        value = float(value)
        sum = sum + value
        n += 1
    except ValueError:
        print('Invalid Input. Please enter a numeric value.\n')

print('\nSum = %.2f' % sum)
```

### Possible Variations

#### Multiple `except` blocks
There could be any number of `except` clauses following a `try` statement.

```python
try:
    STATEMENTS
except SomeException:
    # Code to handle exception
except SomeOtherException:
    # Code to handle exception
except AndAnotherException:
    # Code to handle exception
```

#### Multiple exceptions in one `except` clause
A single `except` clause can also accept multiple exceptions as parenthesized tuple.

```python
try:
    STATEMENTS
except (RuntimeError, TypeError, NameError):
    # Code to handle exception
```

#### The exception instance
You can get the instance of the actual error or exception object using the following syntax.

```python
try:
    STATEMENTS
except SomeException as e:
    # Do something with this `e`
```
## Raising Exceptions
We might need to raise exceptions ourselves when something unexpected happens in our program.

We can use the `raise` keyword to raise exceptions like this:
```python
raise Exception('Hey, this was a test exception.')
raise ValueError('Hey, this was another exception.')
```

The only argument required for the `raise` keyword is the exception itself. This could be either an exception instance or exception class(a class that derives from Exception).

## Built-in Exceptions
There are various types of exceptions in python. Check [the official docs](https://docs.python.org/3/library/exceptions.html) to know about the Built-in Exceptions in python.

## Exercises
1. Improvements on the program to find the area of circle.
    - Move the logic to compute the area to a function
    - Handle runtime exceptions
    - Ability to try again in case of invalid input.

2. Improvements on the program we did to compute the age of the user by checking his date of birth.
    - Refactor it using functions.
    - Handle runtime exceptions.
    - Ability to try again in case of invalid input.

3. Improvements on the program to parse out the value of `m` and `c` from the equation of line `y = mx + c`
    - Refactor the logic for parsing the equation to a function
    - Take two user inputs: equation of two lines
    - Write a function to get the intersection of two lines
    - Write a function to get the angle between two lines
    - Print angle between two lines and the point of intersection
    - Print if they're parallel or perpendicular to each other
    - Handle runtime exceptions.
    - Ability to try again in case of invalid input.

4. Program to ask for a filename and read the contents of the file and print it on the screen. Ensure there are no unhandled exceptions.


## Read More?
Want to read more? Go through these links.
1. https://docs.python.org/3/tutorial/errors.html
2. https://wiki.python.org/moin/HandlingExceptions
3. https://docs.python.org/3/library/exceptions.html
4. http://stackoverflow.com/questions/730764/try-except-in-python-how-do-you-properly-ignore-exceptions
5. https://www.tutorialspoint.com/python/python_exceptions.htm
