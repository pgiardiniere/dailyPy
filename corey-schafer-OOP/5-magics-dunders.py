class Empty:
    foo = 42


class Employee:
    raise_amount = 1.04
    num_employees = 0

    # spoken word 'dunder init' denotes __init__()
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Good practice: return some Python code which recreates instance
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(
            self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


empty = Empty()
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)


# Should always implement: __repr__ and __str__
# __repr__():
#   An unambiguous REPResentation of an object.
#   Used for debug, logs, etc.
#   Seen by developers.

# __str__():
#   a readable representation of an object.
#   Used for general output.
#   Seen by end-users.


# __str__() behavior when print(object) is called:
#   If a __str__() dunder is defined, it will print that
#   If no __str__() dunder is defined, then __str__() method calls __repr__()
#   If no __repr__() dunder is defined, then __str__() method returns
#       the object type and its memory address

print(empty)
print(emp_1)
print(emp_1.__repr__(), end='\n\n')


# Bonus Dunders: __add__()
# Built-in behavior: Strings do concatenation on + operator.
# Contrived example: Add 2 employees together for combined salary.
print(1 + 2)
print('a' + 'b')
print(emp_1 + emp_2, end='\n\n')

# Bonus Dunders: __len__()
# Built-in behavior: Strings and Lists return their length.
# Contrived example: Return combined length of first and last name.
print('test'.__len__())
print(len('test'))
print(len(emp_1))
