Conditionals and Loops
============================

[Home](https://github.com/kabirbaidhya/learn-python-django-web) | [Slides](https://speakerdeck.com/kabirbaidhya/python-conditionals-and-loops) | [← Prev](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/python/3/lists-and-dictionaries.md) | [Next →](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/python/5/functions-and-lambdas.md)


Hope you're now pretty comfortable with the basic stuffs we've covered in the previous sessions so far. You may want to [check the earlier sessions](https://github.com/kabirbaidhya/learn-python-django-web) if you haven't already.

## Conditionals
[Conditional Statements](http://en.wikipedia.org/wiki/Conditional_%28programming%29) are the basic building blocks of every programming language. And every language offers them in one way or another.

In python the simplest of conditional statements is the `if` statement.

### The `if` statement
The most basic if statement could look like this:

**Syntax**
```python
if CONDITION:
    STATEMENT1
    STATEMENT2
    ...
```

The `CONDITION` could be any valid boolean expression which is evaluated. If it's value is evaluated to be `True` then the statements inside the block are run, if it's not `True` the code block simply is ignored and not run.

You can make use of any kind of [boolean operators](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/python/1/python-variables-types-and-operators.md#comparison-operators) in the condition, all you need to make sure is that the expression produces boolean result.

**Don't forget:**
1. The colon `:` in the `if` block, which actually starts the block.
2. Indentation, which is the part of syntax in python and a must have (unlike C-style languages where it's optional).
3. End of indent means end of the block.


#### Example 1
```python
if input('word: ') == 'Foo':
    print('Great!')
    print('You entered "Foo"')

# Normal statements out of the block
print('Good Bye!')
```

You should see this output if you type in `Foo` in the prompt.
```plain
Great!
You entered "Foo"
Good Bye!
```
However, if you type in something else than `Foo` you should see just this:

```plain
Good Bye!
```

### The `if-else` statement
This is another variation of the `if` statement where you can also provide the block of statements which is to be run when the `CONDITION` is evaluated to be `False`.

**Syntax**
```python
if CONDITION:
    STATEMENT1
    STATEMENT2
    ...
else:
    STATEMENT1
    STATEMENT2
    ...
```

Now, if `CONDITION` is evaluated to be `True` the statements inside the `if` block are run as usual, but if it's evaluated as `False` the statements inside `else` block is run instead.

It is worth noting that no matter what your condition is, only either one of these two blocks are run.

#### Example 2
```python
if input('word: ') == 'Foo':
    print('Great!')
    print('You entered "Foo"')
else:
    print('Hey!')
    print('That was something else')

# Normal statements out of the block
print('Good Bye!')
```

Now, you should still see this output if you type in `Foo` in the prompt.
```plain
Great!
You entered "Foo"
Good Bye!
```
However, if you type in something else than `Foo` you should see:

```plain
Hey!
That was something else
Good Bye!
```

### The `if-elif-else` statement

Sometimes we need to chain multiple conditions and it's possible using the multiple `elif` blocks in the `if-else` statements.

**Syntax**
```python
if CONDITION1:
    STATEMENTS

elif CONDITION2:
    STATEMENTS

elif CONDITION3:
    STATEMENTS
...
else:
    STATEMENTS
```

Here, the conditions are checked one by one, and the first code block for which the condition is evaluated to be `True` will be executed and all other blocks are skipped.

If none of the conditions holds true, the `else` block is executed. And if there isn't any `else` block, nothing happens.

There can be any number of `elif` lines, each followed by an indented block. But only one of the indented blocks is executed and it's the one corresponding to the first True condition, or, if all conditions are False, it is the block after the final else line.

In [other languages](http://en.wikipedia.org/wiki/Conditional_%28programming%29#Else_if) this is known as `if-elseif-else`. **But remember in python it is `elif`, not `elseif`**.


#### Example 3
```python
word = input('word: ')

if word == 'Foo':
    print('Great!')
    print('You entered "Foo"')
elif word == 'Bar':
    print('Wow!')
    print('You entered "Bar"')
elif word == 'Baz':
    print('Awesome!')
    print('You entered "Baz"')
else:
    print('Hey!')
    print('That was something else')

# Normal statements out of the block
print('Good Bye!')
```

Now, try this with different inputs like `Foo`, `Bar`, `Baz` and something else. You should see the variation in the output produced using the `if-elif-else` statement blocks.


```plain
$ python3 units/python/4/example_3.py

word: Foo
Great!
You entered "Foo"
Good Bye!


$ python3 units/python/4/example_3.py
word: Bar
Wow!
You entered "Bar"
Good Bye!


$ python3 units/python/4/example_3.py
word: Baz
Awesome!
You entered "Baz"
Good Bye!


$ python3 units/python/4/example_3.py
word: Test
Hey!
That was something else
Good Bye!
```

## Loops

Loops are the programming constructs that allow us execute or iterate over a statement block multiple times depending upon some condition.

Generally we use two types of loops in python:
 1. While Loop
 2. For Loop

### The `while` loop

The `while` loop is the simplest of all.
It iterates over a block of code as long as the base condition holds true.

**Syntax**
```python
while CONDITION:
    STATEMENTS

```

This `CONDITION` is a boolean expression that keeps the loop running as long as it's value is `True`.

#### Example 4
```python
a = 0
# This will print out numbers 1 to 5
while a < 5:
    a = a + 1
    print(a)
```

#### Example 5
```python
n = 0
sum = 0

# Calculate the sum of 5 numbers entered by user
while n < 5:
    value = input('Enter Number %s: ' % (n + 1))
    sum = sum + float(value)
    n += 1

print('Sum = %.2f' % sum)
```

#### Example 6

```python
# Print Fibonacci series upto n
a = 0
b = 1
n = 25

while a < n:
    print(a)
    (a, b) = (b, a + b)

```

#### Example 7
```python
# Lists and the while loop
names = ['John Doe', 'Jane Doe', 'Johnny Turk', 'Molly Mormon']
i = 0
total_names = len(names)
print('Users:')

while i < total_names:

    # This is same as doing.
    #
    # if i == total_names - 2:
    #     end = ' and\n'
    # else:
    #     end = '\n'
    end = ' and\n' if i == total_names - 2 else '\n'

    print(' - %s' % names[i], end=end)
    i += 1

```

### The `for` loop
The `for` loop in python is a dedicated loop for iterating over a sequence, so it is usually used with sequence data types like strings, lists, and tuples.

**Syntax**
```python
for VARIABLE in SEQUENCE:
    STATEMENTS
```

This would iterate over the given sequence `SEQUENCE` and assigns the value of current item of the sequence under iteration to the `VARIABLE` so that it could be used to reference the current item inside the loop block.

#### Example 8
```python
# Loop over a list of numbers

for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(num)

print('--')

# Do the same thing using range.
for num in range(10):
    print(num + 1)

```

#### Example 9
Let's try redoing our `while` loop with list example with `for` loop.

```python
# Lists and the for loop
names = ['John Doe', 'Jane Doe', 'Johnny Turk', 'Molly Mormon']
print('Users:')

for name in names:
    end = ' and\n' if name == names[-2] else '\n'

    print(' - %s' % name, end=end)
```

#### Index in the `for` loop
Sometimes we do need the value of current index of the loop or the sequence we're looping over. In those cases we can do a little tweak to the syntax to get the index too.

We can use `enumerate()` to get a tuple `(index, value)` instead of the regular loop variable that references to the item of current iteration.

```python
names = ['John Doe', 'Jane Doe', 'Johnny Turk', 'Molly Mormon']

for (index, value) in enumerate(names):
    print(' %d \t %s' %(index, value))

```

#### Loop over dictionaries
And there are situations where we need to iterate over the individual key-value pairs in a dictionary. Using `for` loop for that isn't really different than this.

We can make use of `dict.items()` method of a dictionary object to get a list of tuples for each key value pair in the dictionary.

```python
user = {
    'name': 'John Doe',
    'email': 'johndoe@example.com',
    'phone': '(111) 111-1112',
    'address': '123 6th St. Melbourne, FL 32904',
}

for (key, val) in user.items():
    print(' %s : %s' % (key, val))

```

## Exercises
 1. Program to ask for the age of the person and print out the following depending upon the age.

<small>

   | Age                    | Message                      |
   |------------------------|------------------------------|
   | Less than or is Zero   | Invalid input for age.       |
   | Less than 1 year       | You're an infant             |
   | 2 - 12                 | You're just a kid. |
   | 13 - 19                | You're a teenager. |
   | 20 - 45                | You are adult now. |
   | 46 - 59                | You are middle-aged. |
   | 60+                    | You are old now. |
   | 120+                   | You're too old to still be alive.  |

</small>

 2. Program to ask for a co-ordinate point (x, y). And print in which quadrant it lies in. If it lies in any axes print the name of the axis instead. For eg: (5, 0) should print `X-Axis` but (5, - 5) should print `4st Quadrant`.
 3. Program to calculate the factorial of integer `n` taken from user input.
 4. Program to store a list of several users with information: username, email and password. Ask user name and password from the user and check if the combination of username/password matches with the credentials we have in our predefined list.

## Read More?
Want to read more? Go through these links.
1. https://docs.python.org/3/reference/compound_stmts.html
2. http://www.openbookproject.net/books/bpp4awd/ch04.html
3. http://en.wikipedia.org/wiki/Conditional_%28programming%29
4. http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/ifstatements.html
5. https://en.wikibooks.org/wiki/Python_Programming/Conditional_Statements
6. https://docs.python.org/3/reference/expressions.html#conditional-expressions
