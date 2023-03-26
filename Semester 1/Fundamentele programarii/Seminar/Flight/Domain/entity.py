class FlightException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message


class FlightValidator:
    @staticmethod
    def validate(flight):
        if flight.dep_time > flight.arr_time or flight.arr_time - flight.dep_time < 15:
            raise FlightException("Invalid Flight")


class Flight:
    def __init__(self, id: str, dep_city: str, dep_time: int, arr_city: str, arr_time: int):
        self.__id = id
        self.__dep_city = dep_city
        self.__dep_time = dep_time
        self.__arr_city = arr_city
        self.__arr_time = arr_time

    @property
    def id(self):
        return self.__id

    @property
    def dep_city(self):
        return self.__dep_city

    @property
    def dep_time(self):
        return self.__dep_time

    @property
    def arr_city(self):
        return self.__arr_city

    @property
    def arr_time(self):
        return self.__arr_time

    def __str__(self):
        return f"{self.dep_time // 60}:{self.__dep_time % 60} | {self.__arr_time // 60}:{self.__arr_time % 60} | {self.id} | {self.__dep_city} - {self.__arr_city}"
    def __repr__(self):
        return f"{self.dep_time // 60}:{self.__dep_time % 60} | {self.__arr_time // 60}:{self.__arr_time % 60} | {self.id} | {self.__dep_city} - {self.__arr_city}"

    def __eq__(self, other):
        if other.id == self.id and other.dep_time == self.dep_time and other.arr_time == self.arr_time and other.dep_city == self.dep_city and other.arr_city == self.arr_city:
            return True
        return False
