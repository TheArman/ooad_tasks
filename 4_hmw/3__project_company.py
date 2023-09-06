class Employee:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Project:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self.list_employees = []

    def add_employees(self, employee: Employee, company: 'Company') -> None:
        if employee not in company.employees:
            print('empty')
        self.list_employees.append(employee)

    def list_project_details(self) -> list:
        return self.list_employees

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Company:
    def __init__(self) -> None:
        self.employees = []
        self.projects = []

    def add_project(self, project: Project) -> None:
        self.projects.append(project)

    def add_employees(self, employee: Employee) -> None:
        self.employees.append(employee)

    def show_projects(self):
        print(self.projects)

    def show_employees(self):
        print(self.employees)


employee1 = Employee('Henry')
employee2 = Employee('Sara')
employee3 = Employee('David')

project1 = Project('facebook', 'social media')
project2 = Project('hack_facebook', 'hacking')

company = Company()

company.add_employees(employee1)
company.add_employees(employee2)
company.add_employees(employee3)
company.add_project(project1)
company.add_project(project2)

project1.add_employees(employee1, company)
project2.add_employees(employee2, company)
project2.add_employees(employee3, company)

company.show_employees()
company.show_projects()
print(project2.list_employees)

