def create_student(id, name, grade):
    return {"id": id, "name": name, "grade": grade}


def get_id(student):
    return student["id"]


def set_id(student):
    student["id"] = new_id


def get_name(student):
    return name["name"]


def set_name(student):
    student["name"] = new_name


def get_grade(student):
    return student["grade"]


def set_grade(student):
    student["grade"] = new_grade
