Lists and Dictionaries
============================

Hope you're now pretty comfortable with python basics after all we've gone through [variables, data types, operators](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/python/1/python-variables-types-and-operators.md), and [strings manipulation](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/python/2/strings-and-formatting.md) in the last sessions. You may want to [check](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/python/2/strings-and-formatting.md) them if you haven't yet.

## Lists
List is one of the most common and versatile data structures we use in python when it comes to storing a group of items or values.

You can construct a list in python simply as a list of comma-separated values (items) in between square brackets.

Like this:
```python
>>> numbers = [1, 2, 3, 4, 5, 6, 7]
```

#### Lists Common Operations

Like strings, lists are sequences too and thus support all the operations that [sequences in python](https://docs.python.org/3/glossary.html#term-sequence) support.

For example:
```python
>>> len(numbers)
7
>>> min(numbers)
1
>>> max(numbers)
7
>>> numbers.count(5)
1
>>> 7 in numbers
True
>>> 8 in numbers
False
>>> 0 not in numbers
True
```

Lists do support even concatenation just the way strings do with the `+` operator.
```python
>>> numbers + [8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

```
Check the [common operations](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/python/2/strings-and-formatting.md#common-operations) that lists support just like any other sequence types.

#### Mutating values in the list
Unlike strings, lists are [mutable data types](https://docs.python.org/3/glossary.html#term-mutable); thus it's possible to mutate or change the list like this:

```python
names = ['John Doe', 'Jane Doe', 'Johnny Turk']
# Change the first name in the list
names[0] = 'Foo Bar'
print('Names now:', names)

# Append some more names
names.append('Molly Mormon')
names.append('Joe Bloggs')
print('Names finally:', names)
print('Last name in the list: %s' % names[-1])
```

#### List Methods
The list object support the following methods.

| Method                    | Description                                                       |
|---------------------------|-------------------------------------------------------------------|
| append(x)                 | Add an item to the end of the list.                               |
| insert(i, x)              | Insert an item at a given position.                               |
| remove(x)                 | Remove an item from the list whose value equals to `x`. An error is thrown if the value is not found in the list. |
| pop([i])                  | Remove the item at `i`th position in the list, and return it. If index `i` is not, the last item is removed and returned |
| clear()                   | Remove all items from the list. |
| index(x[, start[, end]])  | Return the first index whose value is `x`. Throws an error if the value is not found in the list. |
| count(x)                  | Count the number of times the value `x` appears in the list. |
| sort(x)                   | Sort the items of the list. |
| reverse()                 | Reverse the items of the list. |
| copy()                    | Return a shallow copy of the list.  |

Check the official docs for [lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) more more information.

#### Try them out
Let's try these methods as well.

```python
>>> names.insert(0, 'Mark Joe')
>>> names
['Mark Joe', 'Foo Bar', 'John Doe', 'Jane Doe', 'Johnny Turk', 'Molly Mormon', 'Joe Bloggs']
>>> names.remove('Foo Bar')
>>> names
['Mark Joe', 'John Doe', 'Jane Doe', 'Johnny Turk', 'Molly Mormon', 'Joe Bloggs']
>>> names.pop()
'Joe Bloggs'
>>> names.pop(0)
'Mark Joe'
>>> names
['John Doe', 'Jane Doe', 'Johnny Turk', 'Molly Mormon']
>>> names.sort()
>>> names
['Jane Doe', 'John Doe', 'Johnny Turk', 'Molly Mormon']
>>> names.index('Molly Mormon')
3
```

#### List Comprehensions
List comprehension is a pythonic way of creating lists in a concise manner based upon the results of some operations or certain conditions.
List comprehensions is one of the most popular features of python lists.

For instance:

```python
# Create a list of squares of numbers upto 10
squares = [x**2 for x in range(10)]

# You can create lists using existing lists.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 ==0]
odd_numbers = [x for x in numbers if x % 2 !=0]

# You can even create new lists by processing existing lists.
words = ['this', 'is', 'just', 'a', 'test']
capitalized_words = [x.capitalize() for x in words]

# Can use it for filtering the list items as well.
words = ['hello', 'world', 'foo', 'bar', 'test', 'python', 'is', 'awesome']
short_words = [x for x in words if len(x) <= 3]
other_words = [x for x in words if x not in short_words]
words_with_e = [x for x in words if x.count('e') >= 1]
```
## Dictionaries


## Exercises
1. Write a program to ask for the marks of 5 different subjects and print the total marks obtained and the total percentage.
2. Write a program to ask for the equation of a line in the form `y = mx + c`. And print the values of slope and y-intercept of the line. (Hint: Use `split()`.)

3. Write a program to ask for the user's date of birth in `YYYY-MM-DD` format and calculate the user's age. (Hint: Use `split()` method to split the date parts.)

## Read More?
Want to read more? Go through these links.
1. https://docs.python.org/3/library/stdtypes.html#old-string-formatting
2. https://pyformat.info/
3. https://www.tutorialspoint.com/python/python_strings.htm
