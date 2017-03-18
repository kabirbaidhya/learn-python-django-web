<!--
$theme: gaia
template: invert-->
###### Python
Strings and Formatting
===

# ![](../../../python-logo-200x200.png)

###### [@kabirbaidhya](https://github.com/kabirbaidhya)

---
<!--
$theme: gaia
template: gaia-->
# Reflections
---
## What we know now
After the previous sessions we know about the following:
1. Variables in Python
2. Data Types
3. Operators and Expressions
4. Git - a little bit more :)

---
# Strings
---
<!--
$theme: gaia
template: default-->

### String

A string is traditionally a sequence of characters. 

Strings are one of the common data types in all programming languages and python is not an exception.

String in Python is handled with `str` object and strings are immutable sequences.

---
### Strings in Python
Strings can be represented in various of ways:

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
---
### Common Operations
The following operations are supported by strings and most of the sequences.

<small>

| Operation	            | Result                                                    |
|-----------------------|-----------------------------------------------------------|
| x in s                | True if an item of s is equal to x, else False            |
| x not in s            | False if an item of s is equal to x, else True            |
| s + t                 | the concatenation of s and t          |
| s * n or n * s        | equivalent to adding s to itself n times          |
| s[i]                  | ith item of s, origin 0           |
| s[i:j]                | slice of s from i to j            |
| s[i:j:k]              | slice of s from i to j with step k            |


</small>

---

### Common Operations

| Operation	            | Result                                                    |
|-----------------------|-----------------------------------------------------------|
| len(s)                | length of s           |
| min(s)                | smallest item of s            |
| max(s)                | largest item of s             |
| s.index(x[, i[, j]])  | index of the first occurrence of x in s (at or after index i and before index j) |
| s.count(x)            | total number of occurrences of x in s	 |

---

### Example 1
```python
s = input('Enter a string: ')

print("No. of characters = %d" % len(s))
print("First Character = %s" % s[0])
print("Last Character = %s" % s[len(s) - 1])

# Count the number of vowels
print("No. of 'a' = %s" % s.count('a'))
print("No. of 'e' = %s" % s.count('e'))
print("No. of 'i' = %s" % s.count('i'))
print("No. of 'o' = %s" % s.count('o'))
print("No. of 'u' = %s" % s.count('u'))

# Calculate Percentage of vowels
total_vowels = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')
percentage = (float(total_vowels) / len(s)) * 100
print("\n%.2f%% are vowels." % percentage)
```
---

<!--
$theme: gaia
template: invert-->
### Exercise 1
###### Write a program to ask for the marks of 5 different subjects and print the total marks obtained and the total percentage.

---
### Exercise 2
###### Write a program to ask for the equation of a line in the form `y = mx + c`. And print the values of slope and y-intercept of the line. (Hint: Use `split()`.)

---
### Exercise 3
###### Write a program to ask for the user's date of birth in `YYYY-MM-DD` format and calculate the user's age. (Hint: Use `split()` method.)
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
1. https://docs.python.org/3/library/stdtypes.html#old-string-formatting
2. https://pyformat.info/
3. https://www.tutorialspoint.com/python/python_strings.htm
---
<!--
$theme: gaia
template: gaia-->
# Thank You
###### [@kabirbaidhya](https://github.com/kabirbaidhya)
###### kabirbaidhya@gmail.com
<!--footer: The slides were created using Marp. https://yhatt.github.io/marp/ -->
