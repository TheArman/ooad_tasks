class Employee:
    employee_id = 1

    def __init__(self, name: str):
        self.name = name
        self.employee_id = Employee.employee_id
        Employee.employee_id += 1

    def set_data(self, name: str):
        self.name = name
        self.employee_id = Employee.employee_id
        Employee.employee_id += 1

    def put_data(self):
        print(f'name is {self.name}, employee_id is {self.employee_id}.')


emp1 = Employee('Dave')
emp2 = Employee('Bob')
emp3 = Employee('James')
emp2.set_data('Kane')
emp1.put_data()
emp2.put_data()
emp3.put_data()
