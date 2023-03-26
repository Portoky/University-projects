from Domain.entity import Flight
from repo.mem_repo import MemoRepo, RepoException


class FileRepo(MemoRepo):
    def __init__(self, file_name, validator):
        super().__init__(validator)
        self.__file_name = file_name
        self.load_file()

    def load_file(self):
        try:
            fin = open(self.__file_name, "rt")
            lines = fin.readlines()
            fin.close()
        except FileNotFoundError:
            raise RepoException("File does not exist")
        except IOError:
            pass


        for line in lines:
            token = line.split(",")
            dep_time = token[2]
            blank = dep_time.find(":")
            dep_hour = int(dep_time[:blank])
            dep_min = int(dep_time[blank+1:])
            dep = dep_hour * 60 + dep_min

            arr_time = token[4]
            blank = arr_time.find(":")
            arr_hour = int(arr_time[:blank])
            arr_min = int(arr_time[blank + 1:])
            arr = arr_hour * 60 + arr_min

            flight = Flight(token[0], token[1], dep, token[3], arr)
            super().add(flight)

    def save_file(self):
        fout = open(self.__file_name, "wt")
        for flight in self.find_all():
            dep_hour = flight.dep_time // 60
            dep_min = flight.dep_time % 60
            dep = f"{dep_hour}:{dep_min}"
            arr_hour = flight.arr_time // 60
            arr_min = flight.arr_time % 60
            arr = f"{arr_hour}:{arr_min}"
            line = f"{flight.id},{flight.dep_city},{dep},{flight.arr_city},{arr} \n"
            fout.write(line)
        fout.close()

    def add(self, flight):
        super().add(flight)
        self.save_file()

    def remove_by_id(self, flight_id):
        super().remove_by_id(flight_id)
        self.save_file()
