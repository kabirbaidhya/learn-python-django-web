Conditionals and Loops
============================

Hope you're now pretty comfortable with the basic stuffs we've covered in the previous sessions so far. You may want to [check the earlier sessions](https://github.com/kabirbaidhya/learn-python-django-web) if you haven't already.

## Conditionals
[Conditional Statements](http://en.wikipedia.org/wiki/Conditional_%28programming%29) are the basic building blocks of every programming language. And every language offers them in one way or another.

In python the simplest of conditional statements is the `if` statement.

### The `if` statement
The most basic if statement could look like this:

**Syntax**
```python
if <CONDITION>:
    STATEMENT1
    STATEMENT2
    ...
```

The `CONDITION` could be any valid boolean expression which is evaluated. If it's value is `True` then the statements inside the block are run, if it's not evaluated as `True` the code block simply is ignored and not run.

You can make use of any kind of [boolean operators](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/python/1/python-variables-types-and-operators.md#comparison-operators) in the condition, all you need to make sure is that the expression produces boolean result.

**Dont' forget:**
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
if <CONDITION>:
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
if <CONDITION1>:
    STATEMENTS

elif <CONDITION2>:
    STATEMENTS

elif <CONDITION3>:
    STATEMENTS
...
else:
    STATEMENTS
```

Here, all the conditions would be checked one by one, and the first block of code for which the condition is evaluated to be `True` will be executed and all other blocks are skipped.

If none of the conditions in the chain are evaluated to be `True` then the `else` block is executed. And if there aren't any `else` block nothing happens.

There can be any number of `elif` lines, each followed by an indented block. (Three happen to be illustrated above.) With this construction exactly one of the indented blocks is executed. It is the one corresponding to the first True condition, or, if all conditions are False, it is the block after the final else line.

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

## Exercises
 1. Write a program to ask for the age of the person and print out the following depending upon the age.


   | Age                    | Message                      |
   |------------------------|------------------------------|
   | Less than or is Zero   | Invalid input for age.       |
   | Less than 1 year       | You're an infant             |
   | 2 - 12                 | You're just a kid. |
   | 13 - 19                | You're a teenager. |
   | 20 - 45                | You are adult now. |
   | 46 - 59                | You are middle-aged. |
   | 60+                    | You are old now. |
   | 120+                   | You're too old to be alive.  |

 2. Write a program to ask for a co-ordinate point (x, y). And print in which quadrant it lies in. If it lies in any axes print the name of the axis instead. For eg: (5, 0) should print 'X-Axis' but (5, - 5) should print '4st Quadrant'.

## Read More?
Want to read more? Go through these links.
1. http://www.openbookproject.net/books/bpp4awd/ch04.html
2. http://en.wikipedia.org/wiki/Conditional_%28programming%29
3. https://en.wikibooks.org/wiki/Python_Programming/Conditional_Statements
4. http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/ifstatements.html
