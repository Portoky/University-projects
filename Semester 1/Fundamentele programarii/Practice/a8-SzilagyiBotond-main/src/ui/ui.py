from src.services.grade_services import GradeServices
from src.services.student_services import StudentServices
from src.services.discipline_services import DisciplineServices
from src.repository.repository_exceptions import RepositoryExceptions

class Console:
    def __init__(self, grade_service, student_service, discipline_service):
        self.__grade_service = grade_service
        self.__student_service = student_service
        self.__discipline_service = discipline_service

    def add_student(self):
        try:
            id=input("What id should he have: ")
            name=input("What is the name: ")
            self.__student_service.add_student(id,name)
        except RepositoryExceptions as re:
            print(re)

    def delete_student(self):
        try:
            id=input("What id: ")
            self.__student_service.delete_student(id)
        except RepositoryExceptions as re:
            print(re)

    def update_student(self):
        try:
            id=input("What id: ")
            name=input("What is the new name: ")
            self.__student_service.update_student(id,name)
        except RepositoryExceptions as re:
            print(re)

    def print_all_student(self):
        try:
            self.__student_service.list_all_student()
        except RepositoryExceptions as re:
            print(re)
    def print_options(self):
        print("1. Manage students")
        print("2. Manage disciplines")
        print("3. Add grade")
        print("4. Display all grades")

    def print_options_for_students(self):
        print("1. Add student")
        print("2. Remove student")
        print("3. Update student")
        print("4. List all students")

    def print_options_for_disciplines(self):
        print("1. Add discipline")
        print("2. Remove discipline")
        print("3. Update discipline")
        print("4. List all disciplines")

    def run_console(self):
        options_for_students={}
        options_for_disciplines={}
