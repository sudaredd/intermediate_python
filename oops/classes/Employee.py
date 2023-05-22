import json
class Employee:
    # class variable
    raise_amt = 1.05
    num_of_employees = 0

    # instance variables
    def __init__(self, first, last,  pay, email=None):
        self.first = first
        self.last = last
        self.pay = pay
        if(email == None):
            self.email = first + '.' + last + '@company.com'
        else:
            self.email = email
        Employee.num_of_employees +=1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return f"Employee({self.first} {self.last} {self.pay})"

    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

import datetime
my_date = datetime.date(2023, 5, 20)
print(Employee.is_workday(my_date))

emp_str_1 = "Dav-Bat-21000"
emp_str_2 = "Srf-Ash-24000"
emp_str_3 = "Jam-Won-32000"

print(Employee.from_string(emp_str_1))
print(repr(Employee.from_string(emp_str_1)))
print(str(Employee.from_string(emp_str_1)))
print(Employee.from_string(emp_str_2))
print(Employee.from_string(emp_str_3))


emp1 = Employee('Sud', 'kas', 12000, 'sud.kas@compny.com')
emp2 = Employee('Test', 'user', 22000, 'Test.user@compny.com')

print(emp1 + emp2)
print(len(emp1))
print(len(emp2))

print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)

Employee.set_raise_amt(1.1)

print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)

print(Employee.num_of_employees)
print(f'emp value {json.dumps(emp1.__dict__)}')
print(emp2.email)

print(emp1.fullname())
print(Employee.fullname(emp1))
print(emp2.fullname())

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)