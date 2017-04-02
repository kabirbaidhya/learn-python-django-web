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
