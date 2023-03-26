"""

@author: radu

 
"""
from ro.ubb.studentsapp.domain.entities import create_student


def add_student(all_students, id, name, grade):
    # todo : check if id is unique
    new_student = create_student(id, name, grade)
    all_students.append(new_student)

