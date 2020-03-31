# Property Decorators enable Getters, Setters, Deleters.
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}'.format(self.first, self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")


# Problem: At initialization, create email. What about name updates?
emp_1 = Employee('John', 'Smith')
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname(), end='\n\n')

emp_1.first = 'Jim'
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname(), end='\n\n')

# Solution: Create a Setter using the @property decorator.
# With @property we define a method, but access like an attribute.


# Problem: Assign first and last name of an Employee via fullname string
#   print(emp_1.fullname())
#   emp_1.fullname = 'Corey Schafer'
#   print(emp_1.fullname)
#       In presenter's notes, that throws an error
#       For me that overwrites the fullname() function with fullname() string
print(emp_1.fullname())
emp_1.fullname = 'Corey Schafer'
print(emp_1.fullname())


# Solution: Create a Getter using the @__ decorator.
