"""

@author: radu

"""
from ro.ubb.studentsapp.domain import operations


def get_command():
    line = input("Input the command you want: ")
    pos = line.find(' ')
    if pos == -1:
        return line, []
    cmd_name = line[:pos]
    args = line[pos+1:]
    args = args.split(',')
    # res = []
    # for arg in args:
    #     res.append(arg.strip())
    args = [arg.strip() for arg in args]
    return cmd_name, args

def add_student(students, id, name, grade):
    try:
        id = int(id)
    except ValueError as e:
        print("ID must be a natural number.", e)
        return
    try:
        print("lol")
        grade = int(grade)
    except ValueError as e:
        # print("Grade must be a natural number.", e)
        raise ValueError("Grade must be a natural number", e)
    print("xd")
    #todo: handle exceptions

    operations.add_student(students, id, name, grade)

def print_all(students):
    print(students)

def solve():
    students = []
    opt = {"add": add_student,
           "print-all": print_all,
        }
    while True:
        cmd, ars = get_command()
        print(ars)
        try:
            opt[cmd](students, *ars)
        except ValueError as e:
            print(e)
        except KeyError as e:
            print("Option not yet implemented", e)
