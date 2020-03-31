class Employee:
    raise_amount = 1.04
    num_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_employees += 1

    def print_fullname(self):
        return print('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        """Use super() instead of Employee(self, ...)
        It's not obvious in Single inheritance, but
        for Multiple inheritance, it's all-but required
        """
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        """Here, we set employees=None default argument because
        we never pass mutable datatypes (lists, dicts) as default args.
        """
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            emp.print_fullname()


# Divide Employee class into Managers and Developers
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

# Since the Developer class has no __init__() method, it runs up the
# chain of inheritance (Resolution Order) until it finds one.

# help dialog contains Method Resolution Order.
# help(Developer)

# If no Developer raise_amount, then inherit Employee raise_amount.
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay, end='\n\n')


# Often use subclasses in order to describe objects with more granularity.
# I.e. they have more attributes not found in parent.
# This necessitates a custom __init__().
print(dev_1.prog_lang)
print(dev_2.prog_lang, end='\n\n')


# Similarly to Developer, create subclass Manager
mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
mgr_1.print_emps(); print()

mgr_1.add_emp(dev_2)
mgr_1.print_emps(); print()

mgr_1.remove_emp(dev_1)
mgr_1.print_emps(); print()


# Python Built-in Methods: isinstance(), issubclass().
print('mgr_1 is a Manager:', isinstance(mgr_1, Manager))
print('mgr_1 is a Employee:', isinstance(mgr_1, Employee))
print('mgr_1 is a Developer:', isinstance(mgr_1, Developer), end='\n\n')

print('Developer is a Employee:', issubclass(Developer, Employee))
print('Manager is a Employee:', issubclass(Manager, Employee))
print('Manager is a Developer:', issubclass(Manager, Developer))
