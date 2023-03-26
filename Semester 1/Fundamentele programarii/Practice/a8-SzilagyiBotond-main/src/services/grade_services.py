from src.repository.grade_repository import GradeRepository
from src.domain.entities import Grade


class GradeServices:
    def __init__(self, grade_repository):
        self.__grade_repository = grade_repository

    def add_grade(self, student_id, discipline_id, grade_value):
        grade = Grade(discipline_id, student_id, grade_value)
        self.__grade_repository.add(grade)

    def delete_grades_associated_to_student(self, student_id):
        for grade in self.__grade_repository.find_all_grades():
            if grade.student_id == student_id:
                self.__grade_repository.delete_grade(grade)

    def delete_grades_associated_to_discipline(self, discipline_id):
        for grade in self.__grade_repository.find_all_grades():
            if grade.discipline_id == discipline_id:
                self.__grade_repository.delete_grade(grade)
