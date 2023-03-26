from src.domain.entities import *
from src.domain.validators import *
from src.repository.student_repository import StudentRepository
from src.repository.discipline_repository import DisciplineRepository
from src.repository.repository_exceptions import RepositoryExceptions


class GradeRepository:
    def __init__(self, grade_validator, discipline_repository, student_repository):
        self.__grade_validator = grade_validator
        self.__all_grades = []
        self.__students = student_repository
        self.__disciplines = discipline_repository

    def find_student_by_id(self, student_id):
        if student_id not in self.__students.find_all_students():
            return None
        return self.__students[student_id]

    def find_discipline_by_id(self, discipline_id):
        if discipline_id not in self.__disciplines.find_all_disciplines():
            return None
        return self.__disciplines[discipline_id]

    def add(self, grade):
        self.__grade_validator.validate(grade)
        # if self.find_student_by_id(grade.student_id) is None or self.find_discipline_by_id(
        #         grade.discipline_id) is None:
        #     raise RepositoryExceptions("Nonexistent id")
        self.__all_grades.append(grade)

    def update(self, grade):
        self.__grade_validator.validate(grade)
        # if self.find_student_by_id(grade.student_id) is not None and self.find_discipline_by_id(
        #         grade.discipline_id) is not None:
        for grades in self.__all_grades:
            if grades.student_id == grade.student_id and grade.discipline_id == grades.discipline_id:
                grades.grade_value = grade.grade_value

    def find_all_grades(self):
        return self.__all_grades

    def delete_grade(self,grade):
        self.__grade_validator.validate(grade)
        if grade not in self.find_all_grades() :
            raise RepositoryExceptions("Nonexistent grade")
        self.__all_grades.pop(grade)


# stud_valid = StudentValidator()
# disc_valid = DisciplineValidator()
# stud_repo = StudentRepository(stud_valid)
# disc_repo = DisciplineRepository(disc_valid)
# grade_valid = GradeValidator()
# stud_repo.save(Student(456,"Boti"))
# disc_repo.add(Discipline(345,"Math"))
# grade_repo = GradeRepository(grade_valid, disc_repo, stud_repo)
# grade = Grade(345, 456, 10)
# print(disc_repo.find_by_id(345))
#
# # print(disc_repo.find_by_id(345))
# # print(stud_repo.find_by_id(456))
# # grade_repo.add(grade)
# for entities in grade_repo.find_all_grades():
#     print(entities)
