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
You may have noticed the `self` keyword in above example. Here `self` is a special variable that are injected as the first argument in all the methods (functions of the objects) defined in the class. This `self` is actually a reference to the instance of the class. This `self` reference is similar to `this` pointer of C++ and `this` reference in JavaScript, C# or Java.

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
You can read more about `decorators` in python [here](https://python.swaroopch.com/more.html#decorator).

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

### Private Attributes / Methods
In python all the class members (attributes and methods) are by default public. In other to make class members `private` you need to prefix them with the double underscore (`__`). Python uses name [name-mangling](https://docs.python.org/3/tutorial/classes.html#private-variables) to ensure they're kept private and are out of the public API.

But it should be kept in mind that true "Private" instance members that cannot be accessed except from inside an object don’t exist in Python.

## Inheritance
Inheritance is one of the popular features of OOP. This allows you to create a class by inheriting attributes and behaviors of an existing class. Inheritance does provide reuse of code and logic.

Inheritance can best pictured using the concept of `type` and `subtype`. The class which inherits from a class is called a sub-class and a class which is being inherited is a base class. The key benefit of inheritance is that whatever functionality the baseclass already has, the child classes can reuse them behind the scenes and they can always add extra features that are specific to only that child class objects.

For instance there could be a generalized class called `Person` from which we can create other classes like `Employee`, `Customer`, `Student`. Now each of these sub-classes have everything the `Person` class already has but they can add their own features in addition to the inherited features. In other words we can say there is an `is-a` relationship in between child class and parent class, such that each instance of a sub class is an instance of the base class too i.e sub-class `is a kind of` parent class.

#### Example 4
```python
class Person:
    # This is a class variable.
    total_count = 0

    def __init__(self, name):
        self.name = name
        # Increment the total count
        Person.total_count += 1

    def greet(self):
        print('{}: Hello'.format(self.name))

    @classmethod
    def print_count(cls):
        print('There are {:d} people so far.'.format(cls.total_count))


class Employee(Person):
    def __init__(self, name, started, company):
        Person.__init__(self, name)
        self.started = started
        self.company = company

    def introduce(self):
        Person.greet(self)
        print('I have started working on {} since {}'.format(
            self.company,
            self.started
        ))


class Student(Person):
    def __init__(self, name, grade, school):
        Person.__init__(self, name)
        self.grade = grade
        self.school = school

    def introduce(self):
        Person.greet(self)
        print('I am a student studying in grade {:d} at {}'.format(self.grade, self.school))


def main():
    person1 = Person('John Doe')
    employee1 = Employee('Mark Joe', '2014-12-05', 'Acme Corp.')
    student1 = Student('Jane Doe', 5, 'The Abc School')

    person1.greet()
    employee1.introduce()
    student1.introduce()

main()
```
## Exercises
1. Implement a Stack using a class under `datastructures` module. It should have methods: `push`, `pop`, `top`, `size` and `toList`.
2. Implement a Queue using a class under `datastructures` module. It should have methods: `enqueue`, `dequeue`, `size`, and `toList`.
3. Make use of inheritance to de-duplicate the code for `size` & `toList` for above classes.

## Building a simple app
Simple CLI app for maintaining user information. Create a new git repository for this application.

#### User Information App - Phase II
1. Use a dedicated `User` class instead of using plain dictionary for storing user entries


## Read More?
Want to read more? Go through these links.
 1. https://docs.python.org/3/tutorial/classes.html
 2. http://anandology.com/python-practice-book/object_oriented_programming.html
 3. https://python.swaroopch.com/oop.html
 4. https://www.tutorialspoint.com/python/python_classes_objects.htm
 5. https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
 6. http://stackoverflow.com/questions/1301346/what-is-the-meaning-of-a-single-and-a-double-underscore-before-an-object-name
 7. https://learnpythonthehardway.org/book/ex44.html
