class Employee:
    def __init__(self, name: str) -> None:
        self.name = name


class Department:
    def __init__(self, name: str) -> None:
        self.name = name
        self.list_of_employees = []

    def add_employee(self, employee: Employee) -> None:
        self.list_of_employees.append(employee)

    def list_department_details(self):
        print(f'workers: {self.list_of_employees}')

    def remove_employee(self, employee: Employee) -> None:
        if employee not in self.list_of_employees:
            raise ValueError
        self.list_of_employees.remove(employee)


class Company:
    def __init__(self, name):
        self.list_of_departments = []
        self.name = name

    def add_department(self, department: Department) -> None:
        self.list_of_departments.append(department)

    def remove_department(self, department: Department) -> None:
        if department not in self.list_of_departments:
            raise ValueError('Che vor aydpisi department chka!!!')
        self.list_of_departments.remove(department)

    def find_department(self, employee: Employee):
        for i in self.list_of_departments:
            if employee in i.list_of_employees:
                return i
        return None

    def check_employee(self, employee: Employee) -> bool:
        for department in self.list_of_departments:
            if employee in department.list_of_employees:
                return True
        return False

    def set_employee_department(self, employee: Employee, department: Department) -> None:
        if department not in self.list_of_departments:
            raise ValueError('Che vor aydpisi department chka!!!')
        current_department = self.find_department(employee)

        if current_department is department:
            raise ValueError('animast baner')

        if current_department is not None:
            current_department.remove_employee(employee)
        department.add_employee(employee)


employee1 = Employee('Manuel')
employee2 = Employee('Lemvel')
employee3 = Employee('Suso')
employee4 = Employee('Aliq')

department1 = Department('Msi bajanmunq')
department2 = Department('Soki bajanmunq')
department3 = Department('Katnamterqi bajanmunq')

company1 = Company('Yerevan City')

company1.add_department(department1)
company1.add_department(department2)
company1.add_department(department3)

department1.add_employee(employee1)
department1.add_employee(employee2)
company1.set_employee_department(employee3, department2)
