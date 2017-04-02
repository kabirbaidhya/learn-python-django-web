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

