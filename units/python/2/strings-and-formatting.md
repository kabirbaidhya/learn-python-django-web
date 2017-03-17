Strings, Formatting & Operators
============================

In our previous lesson we discussed about Variables, basic data types and operators. If you haven't gone through it [read it here](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/python/1/python-variables-types-and-operators.md).

## Strings
A string is traditionally a sequence of characters. Strings are one of the common data types in all programming languages and python is not an exception.

String in Python is handled with `str` object and strings are immutable sequences.
Strings can be represented in various in a variety of ways:

```python
# Using Single Quotes
my_string1 = 'This is a string'

# Using Double Quotes
my_string2 = "This is a string too".

# Using Triple Quotes (Multiline strings)
my_string3 = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. '''

# You could write it with double quotes as well
my_string3 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. """

```
## String Methods

Following are some of the common string methods supported by `str` objects.

|Method                                 | Description                                                                                   |
|---------------------------------------|-----------------------------------------------------------------------------------------------|
| capitalize()                          | Return a new string with its first character capitalized and the rest lowercased.             |
| endswith(suffix[, start[, end])       | Check if the string ends with the given suffix. Return boolean result `True` or `False`       |
| startswith(prefix[, start[, end]])    | Check if the string starts with the given prefix and return boolean result `True` or `False`  |
| find(sub[, start[, end]])             | Return the first index in the string where substring `sub` is found within `start` to `end` of the string. Return -1 if not found.  |
| strip([chars])                        | Return a new string with the leading and trailing characters removed. The optional `chars` argument defaults to removing whitespace.  |
| swapcase()                            | Return a new string with uppercase characters converted to lowercase and vice versa.          |
| title()                               | Return a new titlecased version of the string where words start with an uppercase character and other letters are lowercased. |
| upper()                               | Return a new uppercased version of the string.                                                |
| lower()                               | Return a new lowercased version of the string.                                                |
| format(*args, **kwargs)               | Perform a string formatting operation and return the formatted string.                                                 |
| replace(old, new[, count])               | Return a new string by replacing all occurrences of substring `old` with `new`. If `count` argument is provided, only `count` number of replacements would be done.                                                 |

The above listed methods are just some handful of common string methods. Check the official docs for the  [full list](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str).

#### Example 1
```python
text = input('Enter a string: ')

print("capitalize()      = ", text.capitalize())
print("strip()           = ", text.strip())
print("swapcase()        = ", text.swapcase())
print("title()           = ", text.title())
print("upper()           = ", text.upper())
print("lower()           = ", text.lower())
print("replace('a', 'b') = ", text.replace('a', 'b'))
print("endswith('foo')   = ", text.endswith('foo'))
print("startswith('bar') = ", text.startswith('bar'))
print("find('foo')       = ", text.find('foo'))

```

## Exercises

## Read More?
Want to read more? Go through these links.
1. https://docs.python.org/3/library/stdtypes.html#old-string-formatting
2. https://pyformat.info/
3. https://www.tutorialspoint.com/python/python_strings.htm
