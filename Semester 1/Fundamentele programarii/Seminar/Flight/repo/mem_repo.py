class RepoException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message


class MemoRepo:
    def __init__(self, validator):
        self.__flights = {}
        self.__validator = validator

    def find_all(self):
        return list(self.__flights.values())

    def find_by_id(self, id: str):
        if id not in self.__flights:
            return None
        return self.__flights[id]

    def add(self, flight):
        self.__validator.validate(flight)
        for existent_flight in self.find_all():
            if existent_flight.dep_city == flight.dep_city:
                if existent_flight.dep_time == flight.dep_time:
                    raise RepoException("An airport cannot handle more operation at one time")
            elif existent_flight.arr_city == flight.arr_city:
                if existent_flight.arr_time == flight.arr_time:
                    raise RepoException("An airport cannot handle more operation at one time")
            elif existent_flight.dep_city == flight.arr_city:
                if existent_flight.dep_time == flight.arr_time:
                    raise RepoException("An airport cannot handle more operation at one time")
            elif existent_flight.arr_city == flight.dep_city:
                if existent_flight.arr_time == flight.dep_time:
                    raise RepoException("An airport cannot handle more operation at one time")

        if self.find_by_id(flight.id) is not None:
            raise RepoException("flight already in repo")
        self.__flights[flight.id] = flight

    def remove_by_id(self, flight_id: str):
        if self.find_by_id(flight_id) is None:
            raise RepoException("Flight not in repo")
        del self.__flights[flight_id]
