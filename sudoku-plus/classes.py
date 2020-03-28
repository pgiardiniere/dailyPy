# Code from:
# https://www.w3schools.com/python/python_classes.asp

class DumbClass:
    x = 5

bc = DumbClass
print("bc.x is ", bc.x)

# The __init__() function is analogous to the role of class Constructor in Java.
# Similarly, Python's "self" argument is analogous to Java's "this" keyword.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

guy = Person("Guy", 22)
print("Person guy is named", guy.name, "and is", guy.age)

# Class Methods:
del(Person)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hi(self):
        print("    Ayyy lmao it's ya boi", self.name)

pers = Person("Guy", 22)
pers.say_hi()


# Note that self is not a keyword, we can break convention and use 'foo'.
class RudePerson:
    def __init__(foo, name, age):
        foo.name = name
        foo.age = age

sam = RudePerson("sam", 14)
print("RudePerson sam is named", sam.name, "and is", sam.age)

# Further Reading on Self in Python3 - from Guido van Fossum himself.
# http://neopythonic.blogspot.com/2008/10/why-explicit-self-has-to-stay.html
