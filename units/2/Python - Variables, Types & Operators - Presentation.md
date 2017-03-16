<!--
$theme: gaia
template: invert-->
###### Python
Variables, Types & Operators
===

# ![](../../python-logo-200x200.png)

###### [@kabirbaidhya](https://github.com/kabirbaidhya)

---
<!--
$theme: gaia
template: gaia-->
# Before We Begin
---
### Reflections
<small>What we've learned from the past lessons.</small>
1. Python - Hello World!
2. Git
3. Version Control
4. GitHub

<small>Note: If you're not aware of these. Read them at https://github.com/kabirbaidhya/learn-python-django-web</small>

---
<!--
$theme: gaia
template: gaia-->
# Variables
---
<!--
$theme: gaia
template: default-->
> A variable is a symbolic name for (or reference to) information. The variable's name represents what information the variable contains.
<!--
footer: http://www.cs.utah.edu/~germain/PPS/Topics/variables.html
-->

---
### For Instance
`foo` and `bar` could be variables that are just symbolic names that represent some information in the memory. 

```python
# Variable foo contains "Some Information"
foo = "Some Information"

# And variable bar contains 15.04
bar = 15.64

# Now variable `foo` can be used to get the reference of that "Some Information"
print("It contains", foo)

# And they could be used in expressions too
print("Result = ", 5 * bar + 2)
```
<!--
footer:
-->

---
<!--
$theme: gaia
template: default-->
### Variables in Python
* Dynamically typed.
* Every variable is an object.
* Names are case sensitive.
* Assigned to a value using `=` operator eg: `foo = 10`.
* Name can contain letters, underscores (`_`) followed by numbers.
* **Naming Convention**: lowercase names using underscore `_` to separate words. eg: `first_name`, `last_name`, etc.
---
### For instance
Let's say we have a numeric value `20.0` and we want to store it as the radius of a circle.
We do that like this.
```python
radius = 20.0
```

<small>**Here,**
 1. `radius` is a variable.
 2. `20.0` is the value assigned to that variable.

</small>

---

### For instance
Suppose that we need to store another constant value `3.14` as pi.

We can do that as well.
```python
PI = 3.14
```

<small>Now, `PI` is another variable that holds 3.14.</small>

---

### Using them in expressions
Let's do some computation with these values we have now.
```
# Values we have
radius = 20.0
PI = 3.14

# Compute area of the circle
area = PI * radius * radius

# Print the results
print("Area of Circle =", area)
```
---
### In a Nutshell

###### A variable is a symbol that stand in for a value
###### in the program.

---
### Example 1
```python
first_name = "Kabir"
last_name = "Baidhya"
home_town = "Kathmandu, Nepal"

print("Hi! I am", first_name, last_name, ".")
print("I'm from", home_town, ".")
```
<small>Output:</small>
```plain
Hi! I am Kabir Baidhya .
I'm from Kathmandu, Nepal .
```
---
<!--
$theme: gaia
template: gaia-->
# Data Types
---
<!--
$theme: gaia
template: default-->
### Buit-in Data types
* **Numeric**: int, float, long
* **Boolean**: bool
* **Sequences**: str, list, tuple, bytes
* **Mappings**: dict
* **Sets**: set, frozen set

---
### Immutable & Mutable types

1. Immutable types
    - <small>int, float, long, str, tuple, frozen set, etc.</small>
2. Mutable types
    - <small>list, dict, set, etc.</small>
---
### Integer
Integers are positive or negative whole numbers with no decimal points.
In python 2.x there are two `int` types: `int` and `long`.

But in python 3.x onwards both have been unified into `int` and it behaves as `long`.

```python
total_lessons = 24
```
---
### Float
They represent real numbers and are written with a decimal point.

```python
percentage = 70.05
```
---
### Boolean
Variables with boolean type can represent only two values `True` or `False`.

```python
success = True
failure = not success
```
---
#### Example 2: Basic data types
```python
an_integer = 6
a_floating_point = 17.60
a_boolean = True
a_string = "Foo"

print("Integer value =", an_integer)
print("Float value =", a_floating_point)
print("Boolean value =", a_boolean)
print("String value =", a_string)
```

<small>Output: </small>
```plain
Integer value = 6
Float value = 17.60
Boolean value = True
String value = Foo
```

---

<!--
$theme: gaia
template: gaia-->
# Operators
---
<!--
$theme: gaia
template: default-->
### Arithmetic Operators

Python supports all the basic arithmetic operators just like any other programming languages.

<small>

|Operator   |  Operation 	| Example	|
|:---------:|---------------|:---------:|
| + 		| Addition    	| a + b 	|
| _ 		| Subtration  	| a - b 	|
| * 		| Multiplication| a * b 	|
| / 		| Division		| a / b 	|
| \**		| Exponentiation| a \** b 	|
| %			| Modulo		| a % b 	|

</small>

---
### Comparison Operators

Common comparison operators in python are `<`, `>`, `==`, `>=`, `<=`, and `!=`.
All of these operators return boolean results.

<small>

|Operator   |  Comparison 					| Example	|
|:---------:|-------------------------------|:---------:|
| &gt; 		| Is greater than				| a &gt; b 	|
| &lt; 		| Is less than					| a &lt; b 	|
| == 		| Is equal to					| a == b 	|
| &gt;= 	| Is greater than or equal to	| a &gt;= b	|
| &lt;=		| Is less than or equal to		| a &lt;= b	|
| !=		| Is not equal to				| a != b 	|

</small>

---
### Logical Operators

All of these operators return boolean results.

<small>

|Operator   |  Operation 				| Example	|
|:---------:|---------------------------|:---------:|
| and 		| Logical AND				| a and b 	|
| or 		| Logical OR				| a or b 	|
| not 		| Logical NOT				| not a 	|

</small>

---
### Example 3
Try these in Python shell.
```python
>>> (1 * 4) + (4 / 2) - (3 * 2)
>>> 7 % 3
>>> 2 ** 3
>>> 1 > 2
>>> 1 >= 1
>>> 1 < 5
>>> 1 <= 5
>>> 7 == 5
>>> 8 != 5
>>> 7 > 2 and 5 < 8
>>> 7 > 10 or 5 < 8
>>> not (5 > 7)
```
---
<!--
$theme: gaia
template: invert-->
### Exercise 1

###### Write a program to calculate the diameter, circumference, and the area of circle using the value of `radius` and constant `PI = 3.14159`.

---
### Exercise 2

###### Write a program to calculate the distance between two points represented by coordinates `(x1, y1)` and `(x2, y2)` respectively.

---
##### Use Distance Formula
# ![](./distance_formula.png)

---
### Exercise 3

###### Write a program to compute the possible values of `x` from a quadratic equation ax<sup>2</sup> + bx + c = 0 (a â‰  0) using the quadratic equation formula.

---
##### Use Quadratic Formula
# ![](./quadratic_formula.png)

---
<!--
$theme: gaia
template: gaia-->
# User Input
---
<!--
$theme: gaia
template: default-->
### Input
Getting the user input is an important part of every program.
In python you can use the `input` function to get the user input easily.

```python
# Get the input and store it in the variable.
name = input("Please enter your name: ")

# Print the entered value.
print("Hi", name)
```
<small>Note: `input` only works in python3. You need to use `raw_input` if you're using python2.</small>

---
<!--
$theme: gaia
template: invert-->
### Exercise 4
###### Make changes in the program you wrote for exercise 1 to get the radius from the user.

---
### Exercise 5
###### Make changes in the program you wrote for exercise 2 to get x1, y1 & x2, y2 from the user.
---
### Exercise 6
###### Make changes in the program you wrote for exercise 3 to get the values of a, b & c from the user.
---
### Exercise 7
###### Write a program that asks for a number and prints if it's an even number or not.

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
1. https://docs.python.org/3.5/tutorial/introduction.html
2. https://www.digitalocean.com/community/tutorials/how-to-use-variables-in-python-3
3. https://learnpythonthehardway.org/book/ex5.html
4. http://www.pythonforbeginners.com/basics/python-variables
5. https://www.learnpython.org/en/Variables_and_Types
---
### More links
6. https://en.wikibooks.org/wiki/Python_Programming/Data_Types
7. https://docs.python.org/3.6/reference/expressions.html#operator-precedence
---
<!--
$theme: gaia
template: gaia-->
# Thank You
###### [@kabirbaidhya](https://github.com/kabirbaidhya)
###### kabirbaidhya@gmail.com
<!--footer: The slides were created using Marp. https://yhatt.github.io/marp/ -->
