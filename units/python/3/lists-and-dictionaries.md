Lists and Dictionaries
============================

Hope you're now pretty comfortable with python basics after all we've gone through [variables, data types, operators](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/python/1/python-variables-types-and-operators.md), and [strings manipulation](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/python/2/strings-and-formatting.md) in the last sessions. You may want to [check](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/python/2/strings-and-formatting.md) them if you haven't yet.

## Lists
List is one of the most common and versatile data structures we use in python when it comes to storing a group of items or values.

You can construct a list in python simply as a list of comma-separated values (items) in between square brackets.

Like this:
```python
numbers = [1, 2, 3, 4, 5, 6, 7]
```

Elements in a list can be of different data types and can contain another (nested) lists as well.
```python
misc_list = [1, 'foo', '2', 'bar', [5, 6, 7]]
```

#### Lists Common Operations

Like strings, lists are sequences too and thus support all the operations that [sequences in python](https://docs.python.org/3/glossary.html#term-sequence) support.

For example:
```python
>>> numbers = [1, 2, 3, 4, 5, 6, 7]
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

##### Example 1
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

# You can join lists using str.join() method
joined_names = '\n'.join(names)
print('\nList of names:')
print(joined_names)
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

##### Example 2

```python
# Create a list of squares of numbers upto 10
squares = [x**2 for x in range(10)]
print('Squares:', squares)

# You can create lists using existing lists.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 ==0]
odd_numbers = [x for x in numbers if x % 2 !=0]
print('Numbers:', numbers)
print('Even numbers:', even_numbers)
print('Odd numbers:', odd_numbers)
```

##### Example 3
```python
# You can even create new lists by processing existing lists.
words = ['this', 'is', 'just', 'a', 'test']
capitalized_words = [x.capitalize() for x in words]

print('Words:', words)
print('Capitalized Words:', capitalized_words)

# Can use it for filtering the list items as well.
words = ['hello', 'world', 'foo', 'bar', 'test', 'python', 'is', 'awesome']
short_words = [x for x in words if len(x) <= 3]
other_words = [x for x in words if x not in short_words]
words_with_e = [x for x in words if x.count('e') >= 1]

print('Words:', words)
print('Short Words:', short_words)
print('Other Words:', other_words)
print('Words with "e":', words_with_e)
```

#### Looping
Looping through list is really simple in python. You can use `for` loop for looping through lists.

##### Example 4
```python
names = ['John Doe', 'Jane Doe', 'Johnny Turk']

print('Names:')

for name in names:
    print(' - %s' % name)

```

#### Misc
You might often want to check if the list is empty. Usually the list is dynamically generated.
You can do that by checking no. of items in the list is zero or not.

##### Example 5
```python
my_list = []

if len(my_list) == 0:
    print('No items on the list.')
else:
    print(my_list)
```

Note: We'll discuss more about loops and conditions in the upcoming sessions.

## Dictionaries
Another most common data structure used in python is a dictionary.
The main difference between sequence types like strings & lists and dictionaries is that sequences are indexed by range of numeric indexes but dictionaries are indexed by keys.

Any immutable data type can be used as keys in dictionaries, usually they are strings and numbers.

You can always think of a dictionary as a set of key value pairs.


##### Example 6
You can create a dictionary like this:

```python
user_info = {
    'name': 'Kabir Baidhya',
    'email': 'kabirbaidhya@gmail.com',
    'address': 'Kathmandu, Nepal'
}

# Accessing key from a dict is just similar to lists.
print('Name: %s' % user_info['name'])
print('Email: %s' % user_info['email'])
print('Address: %s' % user_info['address'])
```

##### Example 7
Since dictionaries are mutable types you can mutate them just like lists.

```python
user_info['name'] = 'Kabir'
user_info['email'] = user_info['email'].replace('@gmail.com', '+1@gmail.com')

# If the key doesn't already exists it would create a new key-value pair.
user_info['dob'] = '1992-07-30'

# And you can store any type of values inside a dict. Even lists.
user_info['hobbies'] = ['Music', 'Travelling', 'Coding']

print(user_info)
```

##### Example 8
You can create a list of dictionaries if you want to store similar information about multiple entities.

```python
# This is a list of dictionaries.
data = [
    {
        'name': 'Kabir Baidhya',
        'email': 'kabirbaidhya@gmail.com'
    },
    {
        'name': 'John Doe',
        'email': 'johndoe@example.com'
    }
]

# Print information from the dictionary
print('Name: %s' % data[1]['name'])
print('Email: %s' % data[1]['email'])
```

#### Common Operations
Following are some of the common dictionary operations.

| Operation                  | Description                                                       |
|---------------------------|-------------------------------------------------------------------|
| len(d)                 | Return the number of items in the dictionary `d`.                               |
| d[key]              | Access/Return the item of dictionary identified by key `key`. An error is thrown if `key` is not found in the dictionary.                                 |
| d[key] = value                 | Set a value in the dictionary identified by `key`. |
| del d[key]                  | Remove the item with key `key` from the dictionary. An error is thrown if `key` does not exists |
| key in d                   | Check if the `key` exists in the dictionary. Return `True` or `False`. |
| key not in d                   | Check if the `key` doesn't exist in the dictionary i.e just the opposite of `key in d`. Return `True` or `False`. |
| clear()                   | Remove all the items from the dictionary. |
| copy()                    | Return a shallow copy of the dictionary.  |

Read more about dictionaries [here](https://docs.python.org/3/library/stdtypes.html#typesmapping).

## Exercises
1. Store a list of at least 20 words in a list. Ask the user to enter a string(partial) and print out the list of suggestions based on whether or not the word starts with the string entered. Note: the suggestion should be case-insensitive. (Hint: List comprehension)
2. Store a list of user information in a list of dictionaries. Each user's information would contain: first & last name, email and address. Ask the user to input an email address. Print the first user's information found by that email address. Print "Email not found" message if user with email not found. (Hint: List comprehension)

## Read More?
Want to read more? Go through these links.
1. https://docs.python.org/3/tutorial/datastructures.html#dictionaries
2. https://docs.python.org/3/library/stdtypes.html#typesmapping
3. https://docs.python.org/3/tutorial/introduction.html#lists
4. https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
