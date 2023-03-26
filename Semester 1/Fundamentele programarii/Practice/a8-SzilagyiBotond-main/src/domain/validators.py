import src.domain.entities


class StudentValidator:
    def validate(self, student):
        if student.id == "":
            raise ValueError("Invalid student id - blank id")
        if student.name == "" or type(student.name) == int:
            raise ValueError("Invalid student name - blank name or wrong type of name")


class DisciplineValidator:
    def validate(self, discipline):
        if discipline.id == "":
            raise ValueError("Invalid discipline id - blank id")
        if discipline.name == "" or type(discipline.name) == int:
            raise ValueError("Invalid discipline name - blank name or wrong type of name")


class GradeValidator:
    def validate(self, grade):
        if grade.student_id == "":
            raise ValueError("Invalid student id - blank id")
        if grade.discipline_id == "":
            raise ValueError("Invalid discipline id - blank id")
        if type(grade.grade_value) != int:
            raise ValueError("Grade is not int type")
        if grade.grade_value < 1 or grade.grade_value > 10:
            raise ValueError("Invalid grade - grade exceeds bounds")

