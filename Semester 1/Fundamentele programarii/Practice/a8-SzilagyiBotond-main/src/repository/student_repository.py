from src.domain.entities import Student
from src.domain.validators import StudentValidator
from src.repository.repository_exceptions import RepositoryExceptions


class StudentRepository:
    def __init__(self, student_validator):
        self.__student_validator = student_validator
        self.__all_students = {}

    def find_all_students(self):
        return list(self.__all_students.values())

    def find_by_id(self, student_id):
        if student_id in self.__all_students:
            return self.__all_students[student_id]
        return None

    def find_by_name(self, student_name):
        result = []
        for students in self.__all_students:
            if self.__all_students[students].name.lower() == student_name.lower():
                result.append(self.__all_students[students])
        if len(result) != 0:
            return result
        return "There is no student"

    def save(self, student):
        self.__student_validator.validate(student)
        if self.find_by_id(student.id) is not None:
            raise RepositoryExceptions("Student id already exists")
        self.__all_students[student.id] = student

    def delete(self, student):
        self.__student_validator.validate(student)
        if self.find_by_id(student.id) is None:
            raise RepositoryExceptions("Student to delete doesn't exist")
        del self.__all_students[student.id]

    def update(self, student):
        self.__student_validator.validate(student)
        if self.find_by_id(student.id) is None:
            raise RepositoryExceptions("Student to update doesn't exist")
        self.__all_students[student.id] = student
