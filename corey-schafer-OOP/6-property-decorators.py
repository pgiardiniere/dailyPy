# Property Decorators enable Getters, Setters, Deleters.
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None


# Problem: At initialization, create email. What about name updates?
# Solution: Create a Getter using the @property decorator for email method.
emp_1 = Employee('John', 'Smith')
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname, end='\n\n')

emp_1.first = 'Jim'
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname, end='\n\n')

# I.e. with @property we define a method, but access like an attribute.


# Problem: Assign first and last name of an Employee via fullname string
# Solution: Create a Setter using the @function.setter decorator.

print(emp_1.fullname)
emp_1.fullname = 'Corey Schafer'
print(emp_1.fullname, end='\n\n')


# The @function.deleter deleter behaves as you'd expect at this point.
print(emp_1.fullname)
del emp_1.fullname
print(emp_1.fullname)
