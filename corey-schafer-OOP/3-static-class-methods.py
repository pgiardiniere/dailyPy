import datetime


class Employee:

    raise_amount = 1.04
    num_employees = 0

    def __init__(self, first, last, pay):
        Employee.num_employees += 1
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def print_fullname(self):
        return print('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        """Convention for alternative constructors: name them 'from_*'."""
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# Instance Methods: Automatically pass Instance as first argument.
# Class Methods: Automatically pass Class as first argument.
# Static Methods: Pass no first argument automatically.

# By default, class methods take the Instance as the first argument.
# To alter this, add the @classmethod Decorator above method.
# "cls" is to classmethod as "self" is to instance method.
emp_1 = Employee('Corey', 'Shafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount, end='\n\n')

Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount, end='\n\n')

# You can run the class method from an instance, but it's silly to do so.
# emp_1.set_raise_amt(1.05)

# Often use class methods as alternative constructors; see from_string().
emp_str_1 = 'John-Doe-9000'
emp_str_2 = 'Steve-Smight-9001'
emp_str_3 = 'John-Doe-30000'

emp_3 = Employee.from_string(emp_str_1)

print(emp_1.first)
print(emp_2.first)
print(emp_3.first, end='\n\n')


# Static Methods:
# Since they implicitly pass no first argument, they act like functions.
# We use static methods due to some logical connection to their class.

# Example: Is a given date a work-day? Import weekday module to discern.
my_date = datetime.date(2020, 3, 30)
print(Employee.is_workday(my_date))
