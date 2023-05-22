from oops.classes.Employee import Employee

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang=None):
        # super().__init__(first, last, pay, first + '.' + last + '@company.com')
        Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        Employee.__init__(self, first, last, pay)
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

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())



dev_1 = Developer('Suda', "kasi", 25000)
print(dev_1.email)
print(help(Developer))

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

dev_1 = Developer('Suda', "kasi", 25000, 'Python dev')
print(dev_1.__dict__)

dev_2 = Developer('Rah', "pill", 25000)

mgr_1 = Manager ('Hect', 'Almda', 95000, [dev_1])
print(mgr_1.email)
mgr_1.print_emp()
mgr_1.add_emp(dev_2)
mgr_1.print_emp()
mgr_1.remove_emp(dev_1)
mgr_1.print_emp()

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Developer))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))

