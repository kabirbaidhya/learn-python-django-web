Functions and Lambdas
============================

[Home](https://github.com/kabirbaidhya/learn-python-django-web) | [Slides](https://speakerdeck.com/kabirbaidhya/python-exception-handling) | [← Prev](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/python/5/functions-and-lambdas.md) | [Next →]()

## Exceptions
When there are errors in your syntax, your code won't run. But even if your syntax is 100% correct and runs fine, there could be cases when you get errors during the runtime of your program. These errors that get triggered in the runtime are called **Exceptions**.

For instance consider this example, when you're trying to divide two numbers, both received from the user input.

```python
a = float(input('First Number: '))
b = float(input('Second Number: '))

# Divide a by b
result = a / b
```
As the user can provide any values for the two input, guess what happens when he provides the second value as zero. It would throw an error `ZeroDivisionError` and the program would halt.

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

Handling exceptions ensures that the program still continues to run regardless of the exceptions caused. To better explain this consider the following improvement to the program where user can try again and the program continues to run until the user wants to exit.

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
Firstly the statements inside the `try` block is are executed one by one. If any of the statement causes any exceptions the rest of the code in the block is skipped.

If it will check if the exception that is caused is there in the `except` clause or not. If yes, then that particular except block is executed.

In case the exception raised is not in the `except` clause it will propagate to the higher level. If that particular exception has no handler even after reaching the highest level then the program terminates with that exception with it's message shown.

If no exception occurs inside the `try` block after execution of the statements in the code block, the `except` blocks are skipped.

### Possible variations

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
## Exercises

## Read More?
Want to read more? Go through these links.
1. https://docs.python.org/3/tutorial/errors.html
2. https://wiki.python.org/moin/HandlingExceptions
