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
| split(sep=None, maxsplit=-1)                               | Splits the string into substring using the `sep` argument as the separator. Return the list of splitted substrings.                                                |
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
print("split(' ')        = ", text.split(' '))
```

## C-Style formatting
You probably remember the `printf` function if you've programmed in C. You can do similar string formatting in Python as well.

You would do something like this.
```python
print("Hello %s!" % name)
```

## Example 2
```python
# Ask the user to enter first and last name.
first_name = input('Your first name: ')
last_name = input('Your last name: ')

print("\nHi %s %s!" % (first_name, last_name))
print("It's nice to meet you.")
```

Following are teh supported conversion types.

| Conversion	| Meaning                                           |
|---------------|---------------------------------------------------|
| 'd'           | Signed integer decimal.                           |
| 'i'           | Signed integer decimal.                           |
| 'o'           | Signed octal value.                               |
| 'u'           | Obsolete type – it is identical to 'd'.           |
| 'x'           | Signed hexadecimal (lowercase).                   |
| 'X'           | Signed hexadecimal (uppercase).                   |
| 'e'           | Floating point exponential format (lowercase).    |
| 'E'           | Floating point exponential format (uppercase).    |
| 'f'           | Floating point decimal format.                    |
| 'F'           | Floating point decimal format.                    |
| 'g'           | Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.	          |
| 'G'           | Floating point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.	          |
| 'c'           | Single character (accepts integer or single character string).	             |
| 'r'           | String (converts any Python object using repr()).	           |
| 's'           | String (converts any Python object using str()).	            |
| 'a'           | String (converts any Python object using ascii()).	          |
| '%'           | No argument is converted, results in a '%' character in the result.         |

For in-depth information about the C-style formatting [check the official docs](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting).

## Exercises
1. Write a program to ask for the equation of a line in the form `y = mx + c`. And print the values of slope and y-intercept of the line. (Hint: Use `split()`.)

2. Write a program to ask for the user's date of birth in `YYYY-MM-DD` format and calculate the user's age. (Hint: Use `split()` method to split the date parts.)

## Read More?
Want to read more? Go through these links.
1. https://docs.python.org/3/library/stdtypes.html#old-string-formatting
2. https://pyformat.info/
3. https://www.tutorialspoint.com/python/python_strings.htm
