class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    def print(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


class Employee(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        # self.name = name
        # self.age = age
        self.employee_id = employee_id
        self.department = department


emp1 = Employee('Bob', 23, 123, 'devops')
emp2 = Employee('Steve', 32, 124, 'programmer')
print(emp1.name)
emp1.name = 'Kim'
print(emp1.name)
