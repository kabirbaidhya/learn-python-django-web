Classes and Objects
============================

[Home](https://github.com/kabirbaidhya/learn-python-django-web) | [Slides](https://speakerdeck.com/kabirbaidhya/python-classes-and-objects) | [← Prev](https://github.com/kabirbaidhya/learn-python-django-web/blob/master/units/python/7/modules-and-packages.md) | [Next →]()

## Object Oriented Programming
Object Oriented Programming(OOP) is a programming paradigm where we organize our program in terms of objects. Here we wrap the data and operations that manipulate those data into a single self-contained bundle called object. In OOP, objects are the central concepts; we visualize the real world entities in our program by creating Objects that resemble the attributes and behaviors of the real world entities to solve the problems.

Python is also an Object Oriented Programming. In python everything is an object, even the fundamental data types like `int`, `float` etc are objects.

## Classes
As we write our program in terms of objects we need someway to structure or define the object like what attributes and behaviors it's going to have. To define a structure of an object, we define a class. It's more like a blueprint or a template from which objects are created.

Once a class is created we can define any number of instances from it, these are called instances of the class or objects of the class.

## Objects
An Object in OOP is a self-contained bundle in which the data and functions that operate on the data, are encapsulated together, providing it's own functionality. An object in the program most likely resembles to the real world entites like `Person`, `Car`, `Vehicle` or could also refer to the concepts like `HTTPRequest`, `Server`, `Client` etc.

An object is an instance of a class, which functions and behaves as defined in it's class. This object or instance, though belonging to the same class, has it's own copy of data and functions bound to it. So, each instance of a class is different after they're created but they do have same structure i.e properties and functions.

## Defining Class in Python
In python we define classes using the `class` keyword.

#### Example 1
Here is a simplest class we can have in python, which is nothing but an empty class wrapper from which we can create objects.

```python
class Person:
    pass

# p1 and p2 are the instances (objects) or the class Person
p1 = Person()
p2 = Person()

print(p1)
print(p2)
```

#### Example 2
This is another class that has some properties and methods.
```python
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print('{} says Hello'.format(self.name))

# Instantiate the objects
person1 = Person('Foo')
person2 = Person('Bar')

# Invoke the methods of these objects
person1.say_hello()
person2.say_hello()
```

### The `self`
You may have noticed the `self` keyword in above example. Here `self` is a special variable that are injected as the first argument in all the methods (functions of the objects) defined in the class. This `self` is actually a reference to the instance of the class.

Above I have mentioned that each instance of a class has a copy of it's own properties. This is how it works, all the attributes of the object is bound to this `self` variable which is a reference to the actual object instance inside the class.

For instance when you call `person1.say_hello()` method, inside the `say_hello` method the first argument `self` would point to the `person1` itself. Similarly when `person2.say_hello()` method is called, the `self` here would point to `person2` object.
Although `self` is always the first argument in the methods of the class, you do not have to provide this explicitly when you invoke  object's methods, python does it automatically for you. So, you only have to pass in rest of the parameters if you have any, which invoking a method.

Also in the methods above we have used the value of `self.name`, which actually uses the object's `name` attribute which is different for each instance of the class. Which instantiating the object we've taken the value of `name` directly from the constructor method (`__init__`). So, when they're created with `person1 = Person('Foo')` the `name` attribute of the `person1` object is set to `Foo` and

### Constructor
The constructor is a special method in classes that gets invoked automatically when a new instance of that class is being created. In the last example you may have seen the `__init__` method. This is the constructor method.

You can use the constructor for initialization of the object as this would be called at the very begininng of the object's lifecycle.

For instance:
When you do `person1 = Person('Foo')`, the `__init__` method would be triggered with the value of `name` argument passed as `Foo`.

Just like any other method definition, the first argument of the `__init__` method should always be `self`.

### Attributes
Attributes are the properties that the objects have in the program.

#### Instance Attributes
Instance attributes are the attributes owned by each instance/object of the class. Each instance has it's own copy of attributes. Although all the instances of the class have same structure or number of attributes their values and memory location where they're stored are different.

#### Class Attributes
Class attributes are the ones which are owned by the class itself and there is only one copy of those attributes for a class no matter how many instances are created from it. These attributes are owned by the class itself and is shared by all it's objects.

### Methods
Methods are the functions that are bound to the objects inside the class.

#### Instance Methods
Instance methods are the ones which are bound the the object instance and are bound with the `self` reference. These methods have `self` as the first argument that references the object for which the method is being called.

For instance this is an example of instance method. They're invoked on objects with `object.method()` syntax.

```python
class Person:
    ...
    def say_hello(self):
        print('{} says Hello'.format(self.name))
    ...
```

#### Class Methods
Class methods are the functions that aren't related to the individual instances of the class. They're owned by the class itself and aren't bound to a any single instance. We can use the `classmethod` decorator to define a class method inside the class.
Class methods are injected with the reference to the class itself as the first argument. So, you can make use of class's attributes from inside class methods but cannot access the instance's properties as it doesn't have access to the `self` object.

For instance:
```python
class Person:
    ...
    @classmethod
    def print_count(cls):
        print('Total Count = {:d}'.format(cls.count))
    ...
```
To invoke a class method is invoked on the class itself like `Person.print_count()` unlike instance methods.

#### Example 3
```python
class Employee:
    # This is a class variable.
    total_count = 0

    def __init__(self, name, started, company):
        self.name = name
        self.started = started
        self.company = company

        # Increment the total count
        Employee.total_count += 1

    def say_hi(self):
        print('Hi! I\'m {}, I have started working on {} since {}'.format(
            self.name,
            self.company,
            self.started
        ))

    @classmethod
    def print_count(cls):
        print('There are {:d} employees so far.'.format(cls.total_count))

emp1 = Employee('John Doe', '2013-01-02', 'Acme Corp.')
emp2 = Employee('Mark Joe', '2014-12-05', 'Acme Corp.')

emp1.say_hi()
emp2.say_hi()
Employee.print_count()
```

## Exercises

## Building a simple app
Simple CLI app for maintaining user information. Create a new git repository for this application.

#### User Information App - Phase I
1. Create a package name `app`
2. Create a module `reader` under `app` that exposes a function `read` to read from a file and return it's contents.
3. Create a module `writer` under `app` that exposes a function `write` to write contents to a file.
4. Write a script `user_entry.py` that asks for user's first_name, last_name, email and address and append it in a list of users (list of dictionaries).
5. Allow users to input any number of entries until he chooses to exit.
6. Persist the data as a JSON encoded string into a data file `data.json` at the time of exit.
7. Write a script `user_list.py` that prints reads the data from the file `data.json`, decodes the JSON back and displays the list of users.
8. Make the `user_entry.py` to append the data to the file without overwriting the existing contents.
9. Refactor Code - Create a module `user_store` under `app` with functions `load`, `get_all`, `append`, `save`.
10. Refactor Code - Use `user_store` to replace the logic in the scripts `user_entry.py` and `user_list.py`.

## Read More?
Want to read more? Go through these links.
 1. https://docs.python.org/3/tutorial/classes.html
 2. http://anandology.com/python-practice-book/object_oriented_programming.html
 3. https://python.swaroopch.com/oop.html
 4. https://www.tutorialspoint.com/python/python_classes_objects.htm
 5. https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
