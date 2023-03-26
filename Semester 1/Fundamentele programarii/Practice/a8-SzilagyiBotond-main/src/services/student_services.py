from src.repository.student_repository import StudentRepository
from src.domain.entities import Student
from src.domain.validators import StudentValidator


class StudentServices:
    def __init__(self, student_repository):
        self.__student_repository = student_repository

    def add_student(self, student_id, student_name):
        student = Student(student_id, student_name)
        self.__student_repository.save(student)

    def delete_student(self, student_id):

        student = self.__student_repository.find_by_id(student_id)
        self.__student_repository.delete(student)

    def list_all_student(self):
        for student in self.__student_repository.find_all_students():
            print(student)

    def update_student(self, student_id, new_name):
        student = Student(student_id, new_name)
        self.__student_repository.update(student)

    def find_student_by_name(self,student_name):
        for student in self.__student_repository.find_by_name(student_name):
            print(student)


# student = Student(345, "Boti")
# student_validator = StudentValidator()
# student_repo = StudentRepository(student_validator)
# student_service = StudentServices(student_repo)
# student_service.add_student(345, "Boti")
# student_service.add_student(355, "Boti")
# student_service.list_all_student()
# student_service.delete_student(345)
# student_service.find_student_by_name("botI")
# student_service.update_student(355,"Sz")
# student_service.list_all_student()
# for entity in student_repo.find_all_students():
#     print(entity)
# student_service.delete_student(Student(344,"Boti"))
# for entity in student_repo.find_all_students():
#     print(entity)
