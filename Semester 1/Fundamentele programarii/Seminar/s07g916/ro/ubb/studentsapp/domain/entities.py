"""

@author: radu

 
"""


def create_student(id, name, grade):
    return {"id": id, "name": name, "grade": grade}


def get_id(student):
    return student["id"]


def set_id(student, new_id):
    student["id"] = new_id


def get_name(student):
    return student["name"]


def set_name(student, new_name):
    student["name"] = new_name


def get_grade(student):
    return student["grade"]


def set_grade(student, new_grade):
    student["grade"] = new_grade
