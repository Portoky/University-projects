from src.domain.entities import Discipline
from src.domain.validators import DisciplineValidator
from src.repository.repository_exceptions import RepositoryExceptions


class DisciplineRepository:
    def __init__(self, discipline_validator):
        self.__discipline_validator = discipline_validator
        self.__all_disciplines = {}

    def find_all_disciplines(self):
        return list(self.__all_disciplines.values())

    def find_by_id(self, discipline_id):
        if discipline_id in self.__all_disciplines:
            return self.__all_disciplines[discipline_id]
        return None

    def find_by_name(self, discipline_name):
        result = []
        for discipline in self.__all_disciplines:
            if self.__all_disciplines[discipline].name.lower() == discipline_name.lower():
                result.append(self.__all_disciplines[discipline])
        if len(result) != 0:
            return result
        return "There is no discipline"

    def add(self, discipline):
        self.__discipline_validator.validate(discipline)
        if self.find_by_id(discipline.id) is not None:
            raise RepositoryExceptions("Discipline id already exists")
        self.__all_disciplines[discipline.id] = discipline

    def delete(self, discipline):
        self.__discipline_validator.validate(discipline)
        if self.find_by_id(discipline.id) is None:
            raise RepositoryExceptions("Discipline to delete doesn't exist")
        del self.__all_disciplines[discipline.id]

    def update(self, discipline):
        self.__discipline_validator.validate(discipline)
        if self.find_by_id(discipline.id) is None:
            raise RepositoryExceptions("Discipline to update doesn't exist")
        self.__all_disciplines[discipline.id] = discipline
