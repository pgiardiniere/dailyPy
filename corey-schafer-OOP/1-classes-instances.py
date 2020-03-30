# All programs are from Corey Schafer's YouTube miniseries on Python OOP.
# https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

# This will primarily be review of concepts covered in 2168's of Java.

# Terminology review:
# Classes have Attributes and Methods,
# which are some Data and Functions, respectively.


class Empty:
    pass


class Employee:
    pass


# Create instances 1 and 2 of Employee class
emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

# ad-hoc give an instanc of employee some attributes with values
emp_1.first = 'corey'
emp_1.last = 'schafer'
emp_1.pay = '50000'
emp_1.email = 'corey.schafer@company.com'

print(emp_1.first)
del(Employee, emp_1, emp_2)


# It's reasonable to want all employee instances to have these attributes.
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def print_fullname(self):
        return print('{} {}'.format(self.first, self.last))


emp_1 = Employee('Corey', 'Shafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# Call a function and method (respectively) which print full name.
print('{} {}'.format(emp_1.first, emp_1.last))
emp_1.print_fullname()
emp_2.print_fullname()

# Call same function from the Class, not instance. Makes 'self' clearer.
Employee.print_fullname(emp_1)
