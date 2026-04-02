# 3. Create a class ‘Employee’ and add salary and increment properties to it.
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
# which changes the value of increment based on the salary.

class Employee:
    def __init__(self, salary):
        self.salary = salary
      
    @property
    def salaryAfterIncrement(self):
          return self.salary
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, value):
        self.salary += value

    
o = Employee(15000)
o.salaryAfterIncrement = 305000
print(o.salary)


