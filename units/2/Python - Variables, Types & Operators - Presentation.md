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
`foo` and `bar` could be variables that are just symbolic names which represents some information in the memory. 

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
    - <small>int, float, long, tuple, byetes, frozen set, etc.</small>
2. Mutable types
    - <small>list, dict, set, etc.</small>
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
# Read More?
---
### Links
1. https://docs.python.org/3.5/tutorial/introduction.html
2. https://www.digitalocean.com/community/tutorials/how-to-use-variables-in-python-3
3. https://learnpythonthehardway.org/book/ex5.html
4. http://www.pythonforbeginners.com/basics/python-variables
5. https://www.learnpython.org/en/Variables_and_Types
---
### More links
6. https://en.wikibooks.org/wiki/Python_Programming/Data_Types
---
<!--
$theme: gaia
template: gaia-->
# Thank You
###### [@kabirbaidhya](https://github.com/kabirbaidhya)
###### kabirbaidhya@gmail.com
<!--footer: The slides were created using Marp. https://yhatt.github.io/marp/ -->
