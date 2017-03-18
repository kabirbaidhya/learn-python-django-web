<!--
$theme: gaia
template: invert-->
###### Python
Lists and Dictionaries
===

# ![](../../../python-logo-200x200.png)

###### [@kabirbaidhya](https://github.com/kabirbaidhya)

---
<!--
$theme: gaia
template: gaia-->
# Reflections
---
## What we know already
After the previous sessions we know:
1. Python basics - Variables, types, operations
2. Strings and Formatting

---
# Lists
---
<!--
$theme: gaia
template: default-->
### Lists
List is one of the most common and versatile data structures we use in python when it comes to storing a group of items or values.

You can construct a list in python simply as a list of comma-separated values (items) in between square brackets.

Like this:
```python
numbers = [1, 2, 3, 4, 5, 6, 7]
```
---
### Can Contain Anything
Elements in a list can be of different data types and can contain another (nested) lists as well.
```python
# Can contain group of random dissimilar elements.
misc_list = [1, 'foo', '2', 77.00, [5, 6, 7], True]

# Can contain nested lists.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7. 8, 9]
]
```
---
### Common Operations

Like strings, lists are sequences too and thus support the operations that [sequences in python](https://docs.python.org/3/glossary.html#term-sequence) support.

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
### For Instance
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
---
### Concatenation
Lists do support even concatenation just the way strings do with the `+` operator.
```python
>>> numbers + [8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
---
### Example 1
It's possible to mutate or change the lists like this:

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
---
### List Methods
The list object support the following methods.

<small>

| Method                    | Description                                                       |
|---------------------------|-------------------------------------------------------------------|
| append(x)                 | Add an item to the end of the list.                               |
| insert(i, x)              | Insert an item at a given position.                               |
| remove(x)                 | Remove an item from the list whose value equals to `x`. An error is thrown if the value is not found in the list. |
| pop([i])                  | Remove the item at `i`th position in the list, and return it. If index `i` is not, the last item is removed and returned |

</small>

---
### List Methods
<small>

| Method                    | Description                                                       |
|---------------------------|-------------------------------------------------------------------|
| clear()                   | Remove all items from the list. |
| index(x[, start[, end]])  | Return the first index whose value is `x`. Throws an error if the value is not found in the list. |
| count(x)                  | Count the number of times the value `x` appears in the list. |
| sort(x)                   | Sort the items of the list. |
| reverse()                 | Reverse the items of the list. |
| copy()                    | Return a shallow copy of the list.  |

Check the official docs for [lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) more more information.

</small>

---
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
```
---
### List Comprehensions
List comprehension is a pythonic way of creating lists in a concise manner based upon the results of some operations or certain conditions.

List comprehensions is one of the most popular features of python lists.

```python
# Create a list of squares of numbers upto 10
squares = [x**2 for x in range(10)]

print('Squares:', squares)
```
---
### Example 2
```python
# You can create lists using existing lists.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 ==0]
odd_numbers = [x for x in numbers if x % 2 !=0]
print('Numbers:', numbers)
print('Even numbers:', even_numbers)
print('Odd numbers:', odd_numbers)
```
---

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
---
### Looping
Looping through list is really simple in python. You can use `for` loop for looping through lists.

```python
names = ['John Doe', 'Jane Doe', 'Johnny Turk']

print('Names:')

for name in names:
    print(' - %s' % name)

```
---

### Example 5
You might often want to check if the list is empty. Usually the list is dynamically generated.
You can do that by checking no. of items in the list is zero or not.

```python
my_list = []

if len(my_list) == 0:
    print('No items on the list.')
else:
    print(my_list)
```
---
<!--
$theme: gaia
template: invert-->
# Exercises
---
### Exercise 1
###### Store a list of at least 20 words in a list. Ask the user to enter a string(partial) and print out the list of suggestions based on whether or not the word starts with the string entered. 
###### Note: the suggestion should be case-insensitive. (Hint: List comprehension).

---
### Exercise 2
###### Store a list of user information in a list of dictionaries. Each user's information would contain: first & last name, email and address. Ask the user to input an email address. Print the first user's information found by that email address. Print "Email not found" message if user with email not found. (Hint: List comprehension)

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
1. https://docs.python.org/3/tutorial/datastructures.html#dictionaries
2. https://docs.python.org/3/library/stdtypes.html#typesmapping
3. https://docs.python.org/3/tutorial/introduction.html#lists
4. https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
---
<!--
$theme: gaia
template: gaia-->
# Thank You
###### [@kabirbaidhya](https://github.com/kabirbaidhya)
###### kabirbaidhya@gmail.com
<!--footer: The slides were created using Marp. https://yhatt.github.io/marp/ -->
