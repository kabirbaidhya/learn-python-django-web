<!--
$theme: gaia
template: invert-->
###### Python
Conditionals and Loops
===

# ![](../../../python-logo-200x200.png)

###### [@kabirbaidhya](https://github.com/kabirbaidhya)

---
<!--
$theme: gaia
template: gaia-->
# Reflections
---
## What we already know
From the last session.

1. Lists
2. Dictionaries


<small>Note: If you're not aware of these. Read them at https://github.com/kabirbaidhya/learn-python-django-web</small>

---
# Conditional Statements
---
<!--
$theme: gaia
template: default-->
### Conditional Statements

- The basic building blocks of every programming language. 
- Every language offers them in one way or another.
- In Python the simplest of conditional statements is the `if` statement.

---
### The `if` statement

```python
if CONDITION:
    STATEMENT1
    STATEMENT2
    ...
```

The `CONDITION` could be any valid expression that results boolean value. 

The statements inside the block are run only if the `CONDITION` holds true else the indented code block will be ignored.

---
### Dont' Forget
1. The colon `:` in the `if` block, which actually starts the block.
2. Indentation, which is the part of syntax in python and a must have (unlike C-style languages where it's optional).
3. End of indent means end of the block.
---


### Example 1
```python
if input('word: ') == 'Foo':
    print('Great!')
    print('You entered "Foo"')

# Normal statements out of the block
print('Good Bye!')
```

---
### The `if-else` statement
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

The statements inside the `if` block are run if the `CONDITION` holds true otherwise the code from the `else` block will be run.

Only either one of these two blocks are run.

---
### Example 2
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
---
### The `if-elif-else` statement
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
---
### The `if-elif-else` statement
* Conditions are checked one by one, and the first code block for which the condition results  `True` will be executed and all other blocks are skipped.
* If none of the conditions holds true, the `else` block is executed. And if there isn't any `else` block, nothing happens.
* There can be any number of `elif` blocks. But only one of the block is run no matter what.
* **Remember it is `elif`, not `elseif`**
---
### Example 3
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
---
<!--
$theme: gaia
template: gaia-->
# Loops
---
<!--
$theme: gaia
template: default-->
### Loops in Python
Loops are the programming constructs that allow us execute or iterate over a statement block multiple times depending upon some condition.

Generally we use two types of loops in python:
 1. While Loop
 2. For Loop

---
### The `while` loop

It's the simplest of all.

<small>**Syntax**</small>

```python
while CONDITION:
    STATEMENTS

```

It iterates over a block of code as long as the base condition holds true.

---
### Example 4
```python
a = 0

# This will print out numbers 1 to 5
while a < 5:
    a = a + 1
    print(a)
```
---
### Example 5
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
---
### Example 6

```python
# Print Fibonacci series upto n
a = 0
b = 1
n = 25

while a < n:
    print(a)
    (a, b) = (b, a + b)

```
---
### Example 7
```python
# Lists and the while loop
names = ['John Doe', 'Jane Doe', 'Johnny Turk']
i = 0
total_names = len(names)
print('Users:')

while i < total_names:
    end = ' and\n' if i == total_names - 2 else '\n'
    print(' - %s' % names[i], end=end)
    i += 1

```
---
### The `for` loop

Loop dedicated for iterating over a sequence types.

<small>**Syntax**</small>
```python
for VARIABLE in SEQUENCE:
    STATEMENTS
```

Iterates over the given sequence `SEQUENCE`.

The `VARIABLE` would hold the current item over each iteration of the loop.

---
### Example 8
```python
# Loop over a list of numbers

for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(num)

print('--')

# Do the same thing using range.
for num in range(10):
    print(num + 1)

```
---
### Example 9
Redoing the last `while` example with `for` loop.

```python
# Lists and the for loop
names = ['John Doe', 'Jane Doe', 'Johnny Turk']
print('Users:')

for name in names:
    end = ' and\n' if name == names[-2] else '\n'

    print(' - %s' % name, end=end)
```

---
### Index in the `for` loop
Use `enumerate()` to get a tuple `(index, value)` instead of regular item of sequence.

```python
names = ['John Doe', 'Jane Doe', 'Johnny Turk']


for (index, value) in enumerate(names):
    print(' %d \t %s' %(index, value))

```

---
### Loop over dictionaries
Use `dict.items()` method to get a list of tuples for each key value pair in the dictionary.

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
---
<!--
$theme: gaia
template: invert-->
# Exercises
---
### Exercise 1
######  1. Program to ask for the age of the person and print out the following depending upon the age.

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

---

### Exercise 2
######  Program to ask for a co-ordinate point `(x, y)`. And print in which quadrant it lies in. If it lies in any axes print the name of the axis instead. For eg: `(5, 0)` should print `'X-Axis'` but `(5, - 5)` should print `'4st Quadrant'`.

---
### Exercise 3
######  Program to calculate the factorial of integer `n` taken from user input.

---
### Exercise 4
######  Program to store a list of several users with information: username, email and password. Ask user name and password from the user and check if the combination of username/password matches with the credentials we have in our predefined list.

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
1. https://docs.python.org/3/reference/compound_stmts.html
2. http://www.openbookproject.net/books/bpp4awd/ch04.html
3. http://en.wikipedia.org/wiki/Conditional_%28programming%29
4. http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/ifstatements.html
---
### More Links
5. https://en.wikibooks.org/wiki/Python_Programming/Conditional_Statements
6. https://docs.python.org/3/reference/expressions.html#conditional-expressions
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
