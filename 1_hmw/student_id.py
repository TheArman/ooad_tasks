class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.__student_id = student_id

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.name

    def get_student_id(self):
        return self.__student_id


student0 = Student('arman', 22, 7291)

try:
    print(student0.student_id)
except AttributeError:
    print('Shat txur error(sxalanq):')
