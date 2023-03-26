from src.repository.discipline_repository import DisciplineRepository
from src.domain.entities import Discipline
from src.domain.validators import DisciplineValidator
from src.services.grade_services import GradeServices


class DisciplineServices:
    def __init__(self, discipline_repository):
        self.__discipline_repository = discipline_repository

    def add_discipline(self, discipline_id, discipline_name):
        discipline = Discipline(discipline_id, discipline_name)
        self.__discipline_repository.save(discipline)

    def delete_discipline(self, discipline_id, discipline_name):
        discipline = Discipline(discipline_id, discipline_name)
        self.__discipline_repository.delete(discipline)

    def list_all_discipline(self):
        for discipline in self.__discipline_repository.find_all_disciplines():
            print(discipline)

    def update_discipline(self, discipline_id, new_discipline_name):
        discipline = Discipline(discipline_id, new_discipline_name)
        self.__discipline_repository.update(discipline)

    def find_discipline_by_name(self, discipline_name):
        for discipline in self.__discipline_repository.find_by_name(discipline_name):
            print(discipline)
