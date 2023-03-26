"""

@author: radu

"""
from ro.ubb.studentsapp.domain.entities import create_student

def add_student(students, id, name, grade):
    students.append(create_student(id, name, grade))
    #todo: check if the id is unique

