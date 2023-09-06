class Course:
    def __init__(self, name: str, credit: float) -> None:
        self.name = name
        self.credit = credit
        self.list_students = []

    def add_student(self, name: str) -> None:
        self.list_students.append(name)

    def students_details(self) -> list:
        return self.list_students

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name


class Department:
    def __init__(self) -> None:
        self.list_of_course = []

    def add_course(self, course: Course) -> None:
        self.list_of_course.append(course)

    def remove_course(self, course: Course):
        if course not in self.list_of_course:
            print('empty')
        self.list_of_course.remove(course)

    def courses_details(self) -> list:
        return self.list_of_course


course1 = Course('Course 1', 12)
course2 = Course('Course 2', 18)

department = Department()
course1.add_student('Bob')
course1.add_student('Steve')

department.add_course(course1)
department.add_course(course2)
print(department.course_details())
department.remove(course1)
print(department.course_details())
print(course1.students_details())
