class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def print_fullname(self):
        return print('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)


emp_1 = Employee('Corey', 'Shafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
del(Employee, emp_1, emp_2)

# Class variables are one level above instance variables.
# For example, a global flat-rate raise applied to all employees.

# We could do this with a method, apply_raise(), and hard-code amount 1.04.
# But we can't access the raise amount easily via dot notation.
# And we can't update the raise amount easily similarly.

# A better idea is to code 1.04 as a Class Variable.


class Employee:
    raise_amount = 1.04
    num_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        # Access class attribute directly through class
        Employee.num_employees += 1

    def print_fullname(self):
        return print('{} {}'.format(self.first, self.last))

    # Access class attribute indirectly through instance
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Corey', 'Shafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.pay)
print(emp_2.pay)
emp_1.apply_raise()
emp_2.apply_raise()
print(emp_1.pay)
print(emp_2.pay, end='\n\n')

# Why does it work? Because instance finds no instance-level attribute,
# it reads the parent class (and then any super classes) for it.

# See the namespaces for the instance and class, respectively.
print(emp_1.__dict__, end='\n\n')
print(Employee.__dict__, end='\n\n')

emp_1.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount, end='\n\n')

print(emp_1.__dict__, end='\n\n')

# Hence, for class-level Attribute raise_amount, it makes sense
# to access that indirectly via 'self' in class methods.
# -This allows instances and sub-classes to override class constant.
# -This allows class methods to use attributes defined at multiple levels.

# But for class-level Attribute num_employees, it makes sense
# to access that directly, as we do not want instance overriding.
