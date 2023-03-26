from dataclasses import dataclass


@dataclass
class Student:
    __student_id: str
    __student_name: str

    def __str__(self):
        return str(self.__student_id) + ": " + str(self.__student_name)

    @property
    def id(self):
        return self.__student_id

    @id.setter
    def id(self, new_id):
        self.__student_id = new_id

    @property
    def name(self):
        return self.__student_name

    @name.setter
    def name(self, new_name):
        self.__student_name = new_name


@dataclass
class Discipline:
    __discipline_id: str
    __discipline_name: str

    @property
    def id(self):
        return self.__discipline_id

    @id.setter
    def id(self, new_id):
        self.__discipline_id = new_id

    @property
    def name(self):
        return self.__discipline_name

    @name.setter
    def name(self, new_name):
        self.__discipline_name = new_name

    def __str__(self):
        return str(self.__discipline_id) + ": " + str(self.__discipline_name)


@dataclass
class Grade:
    __discipline_id: str
    __student_id: str
    __grade_value: str

    @property
    def discipline_id(self):
        return self.__discipline_id

    @discipline_id.setter
    def discipline_id(self, new_id):
        self.__discipline_id = new_id

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, new_id):
        self.__student_id = new_id

    @property
    def grade_value(self):
        return self.__grade_value

    @grade_value.setter
    def grade_value(self, new_grade):
        self.__grade_value = new_grade

    def __str__(self):
        return "Discipline id: " + str(self.__discipline_id) + ", student id: " + str(
            self.__student_id) + ", grade: " + str(self.__grade_value)


# student = Student(345, "fafasdas")
# dic = {student.id: student}
# student2=Student("f324r234","dsad")
# dic[student2.id]=student2
# print(list(dic.values()))
# print(dic[student2.id])

