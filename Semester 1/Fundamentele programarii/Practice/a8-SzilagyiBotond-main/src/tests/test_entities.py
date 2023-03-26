import unittest
from src.domain.entities import *


class TestGrade(unittest.TestCase):
    def runTest(self):
        self.grade = Grade(1234, 5678, 10)
        self.assertEqual(self.grade.grade_value, 10, "should be 10")
        self.assertEqual(self.grade.discipline_id, 1234, "should be 1234")
        self.assertEqual(self.grade.student_id, 5678, "should be 5678")


class TestDiscipline(unittest.TestCase):
    def runTest(self):
        self.discipline = Discipline(1234, "Chemistry")
        self.assertEqual(self.discipline.id, 1234, "should be 1234")
        self.assertEqual(self.discipline.name, "Chemistry", "should be 12345")


class TestStudent(unittest.TestCase):
    def runTest(self):
        self.student = Student(1234, "Lázár Róbert")
        self.assertEqual(self.student.name, "Lázár Róbert", "should be Lázár Róbert")
        self.assertEqual(self.student.id, 1234, "should be 1234")


